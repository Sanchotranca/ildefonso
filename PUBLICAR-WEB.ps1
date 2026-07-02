# ================================================================
#  PUBLICAR-WEB.ps1   (CAPA DE CONTENCION: publicar la web)
#  FTP/FTPS con PowerShell PURO (sin WinSCP).
#
#  Hace, en orden:
#    1) BACKUP del sitio EN VIVO  -> _backups\FECHA\   (si falla, NO sube)
#    2) VISTA PREVIA de lo que se subiria
#    3) Pide escribir  PUBLICAR  para confirmar
#    4) SUBE los archivos por FTPS
#    5) VERIFICA (compara tamanos + comprueba que la home responde 200)
#
#  La contrasena se pide al ejecutar; NO se guarda en el archivo.
# ================================================================
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

# ---------- CONFIG (editar solo si cambian los datos del hosting) ----------
$ftpHost    = 'cp7027.webempresa.eu'                 # host FTP
$ftpUser    = 'MLAA@residenciasanildefonso.es'       # usuario FTP
$localDir   = $PSScriptRoot                           # sube ESTA carpeta
$homeUrl    = 'https://www.residenciasanildefonso.es' # para verificar al final

# Carpetas/archivos que NO se suben (herramientas y documentacion interna)
$excludeDirs   = @('.git','.github','scripts','node_modules','_backups','contenido-backup')
$excludeExt    = @('.ps1','.bat','.md')
$excludeNames  = @('.cursorrules','.cpanel.yml','.gitignore','.gitattributes','package.json','package-lock.json','git-log.txt')
# ---------------------------------------------------------------------------

Write-Host ''
Write-Host '===========================================================' -ForegroundColor Cyan
Write-Host '   PUBLICAR WEB  (FTPS - PowerShell puro, sin WinSCP)      ' -ForegroundColor Cyan
Write-Host '===========================================================' -ForegroundColor Cyan
Write-Host "Origen : $localDir"
Write-Host "Destino: ftp://$ftpHost  (usuario $ftpUser)"
Write-Host ''

# TLS 1.2 y aceptar el certificado del hosting para esta sesion
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
[Net.ServicePointManager]::ServerCertificateValidationCallback = { $true }

# ---- Credenciales (contrasena en memoria, no en disco) ----
$sec  = Read-Host 'Contrasena FTP' -AsSecureString
if (-not $sec -or $sec.Length -eq 0) { Write-Host 'Sin contrasena. Cancelado.' -ForegroundColor Yellow; Read-Host 'Enter para salir'; exit 1 }
$cred = New-Object System.Net.NetworkCredential($ftpUser, $sec)

# ---- Funciones FTP ----
function New-FtpReq($uri, $method) {
    $r = [System.Net.FtpWebRequest]::Create($uri)
    $r.Credentials = $cred
    $r.EnableSsl   = $true
    $r.UsePassive  = $true
    $r.UseBinary   = $true
    $r.KeepAlive   = $false
    $r.Method      = $method
    return $r
}
function Get-FtpList($remoteDir) {
    $uri = "ftp://$ftpHost/$remoteDir"
    $r = New-FtpReq $uri ([System.Net.WebRequestMethods+Ftp]::ListDirectoryDetails)
    $resp = $r.GetResponse(); $sr = New-Object IO.StreamReader($resp.GetResponseStream())
    $txt = $sr.ReadToEnd(); $sr.Close(); $resp.Close()
    return ($txt -split "`r?`n") | Where-Object { $_ -ne '' }
}
function Download-FtpFile($remotePath, $localFile) {
    $uri = "ftp://$ftpHost/$remotePath"
    $r = New-FtpReq $uri ([System.Net.WebRequestMethods+Ftp]::DownloadFile)
    $resp = $r.GetResponse(); $rs = $resp.GetResponseStream()
    $fs = [IO.File]::Create($localFile); $rs.CopyTo($fs); $fs.Close(); $rs.Close(); $resp.Close()
}
function Get-FtpSize($remotePath) {
    try { $r = New-FtpReq "ftp://$ftpHost/$remotePath" ([System.Net.WebRequestMethods+Ftp]::GetFileSize)
          $resp = $r.GetResponse(); $sz = $resp.ContentLength; $resp.Close(); return $sz } catch { return -1 }
}
function Ensure-RemoteDirChain($remoteFilePath) {
    $idx = $remoteFilePath.LastIndexOf('/')
    if ($idx -lt 0) { return }
    $dir = $remoteFilePath.Substring(0, $idx)
    $acc = ''
    foreach ($seg in ($dir -split '/')) {
        if (-not $seg) { continue }
        $acc = if ($acc) { "$acc/$seg" } else { $seg }
        try { $r = New-FtpReq "ftp://$ftpHost/$acc" ([System.Net.WebRequestMethods+Ftp]::MakeDirectory); $r.GetResponse().Close() } catch {}
    }
}
function Upload-FtpFile($localFile, $remotePath) {
    Ensure-RemoteDirChain $remotePath
    $r = New-FtpReq "ftp://$ftpHost/$remotePath" ([System.Net.WebRequestMethods+Ftp]::UploadFile)
    $bytes = [IO.File]::ReadAllBytes($localFile)
    $r.ContentLength = $bytes.Length
    $rs = $r.GetRequestStream(); $rs.Write($bytes,0,$bytes.Length); $rs.Close()
    $resp = $r.GetResponse(); $resp.Close()
}
function Backup-Remote($remoteDir, $destDir) {
    New-Item -ItemType Directory -Force -Path $destDir | Out-Null
    foreach ($line in (Get-FtpList $remoteDir)) {
        $tok  = $line -split '\s+', 9
        if ($tok.Count -lt 9) { continue }
        $name = $tok[8]
        if ($name -eq '.' -or $name -eq '..') { continue }
        $isDir = $tok[0].StartsWith('d')
        $rp = if ($remoteDir) { "$remoteDir/$name" } else { $name }
        if ($isDir) { Backup-Remote $rp (Join-Path $destDir $name) }
        else { Download-FtpFile $rp (Join-Path $destDir $name) }
    }
}

# ---- 0) Probar conexion ----
Write-Host 'Probando conexion FTPS...' -NoNewline
try { Get-FtpList '' | Out-Null; Write-Host ' OK' -ForegroundColor Green }
catch { Write-Host ' FALLO' -ForegroundColor Red; Write-Host $_.Exception.Message -ForegroundColor Red
        Write-Host 'Revisa host/usuario/contrasena. No se ha tocado nada.'; Read-Host 'Enter para salir'; exit 1 }

# ---- 1) BACKUP del sitio en vivo (si falla, NO se sube nada) ----
$stamp     = Get-Date -Format 'yyyy-MM-dd_HHmm'
$backupDir = Join-Path $localDir "_backups\$stamp"
Write-Host ''
Write-Host "CONTENCION 1/2: descargando copia del sitio en vivo a  _backups\$stamp ..." -ForegroundColor Cyan
try { Backup-Remote '' $backupDir }
catch { Write-Host 'ERROR haciendo el backup del sitio en vivo. NO se sube nada (contencion).' -ForegroundColor Red
        Write-Host $_.Exception.Message -ForegroundColor Red; Read-Host 'Enter para salir'; exit 1 }
$backupCount = (Get-ChildItem -Recurse -File $backupDir | Measure-Object).Count
Write-Host "Backup OK: $backupCount archivos guardados en  $backupDir" -ForegroundColor Green

# ---- 2) Preparar lista local y VISTA PREVIA ----
$files = Get-ChildItem -Recurse -File $localDir | Where-Object {
    $rel = $_.FullName.Substring($localDir.Length).TrimStart('\')
    $segs = $rel -split '[\\/]'
    (-not ($segs | Where-Object { $excludeDirs -contains $_ })) -and
    ($excludeExt   -notcontains $_.Extension.ToLower()) -and
    ($excludeNames -notcontains $_.Name)
}
$totalKB = [math]::Round((($files | Measure-Object Length -Sum).Sum / 1KB), 0)
Write-Host ''
Write-Host "CONTENCION 2/2: VISTA PREVIA - se subirian $($files.Count) archivos ($totalKB KB):" -ForegroundColor Cyan
$files | Select-Object -First 25 | ForEach-Object { Write-Host ('  ' + $_.FullName.Substring($localDir.Length).TrimStart('\')) }
if ($files.Count -gt 25) { Write-Host ('  ... y ' + ($files.Count - 25) + ' mas') }

# ---- 3) Confirmacion explicita ----
Write-Host ''
Write-Host 'Nada se ha subido todavia. El backup ya esta guardado.' -ForegroundColor Yellow
$ok = Read-Host 'Escribe  PUBLICAR  para subir a la web  (cualquier otra cosa = cancelar)'
if ($ok -ne 'PUBLICAR') { Write-Host 'CANCELADO. La web NO se ha tocado (y tienes el backup).' -ForegroundColor Yellow; Read-Host 'Enter para salir'; exit 0 }

# ---- 4) SUBIR ----
Write-Host ''
Write-Host 'Subiendo...' -ForegroundColor Cyan
$subidos = 0; $fallos = 0
foreach ($f in $files) {
    $rel = ($f.FullName.Substring($localDir.Length).TrimStart('\')) -replace '\\','/'
    try { Upload-FtpFile $f.FullName $rel; $subidos++; Write-Host ("  OK  $rel") }
    catch { $fallos++; Write-Host ("  FALLO  $rel  -> " + $_.Exception.Message) -ForegroundColor Red }
}
Write-Host ''
$colFallos = 'Green'; if ($fallos -gt 0) { $colFallos = 'Yellow' }
Write-Host "Subidos: $subidos   Fallos: $fallos" -ForegroundColor $colFallos

# ---- 5) VERIFICAR ----
Write-Host ''
Write-Host 'Verificando (tamanos remoto vs local)...' -ForegroundColor Cyan
$okv = 0; $badv = 0
foreach ($f in $files) {
    $rel = ($f.FullName.Substring($localDir.Length).TrimStart('\')) -replace '\\','/'
    $rs = Get-FtpSize $rel
    if ($rs -eq $f.Length) { $okv++ } else { $badv++; Write-Host ("  DIFERENCIA  $rel  (local $($f.Length) / remoto $rs)") -ForegroundColor Yellow }
}
Write-Host "Coinciden: $okv   No coinciden: $badv"
Write-Host ''
Write-Host 'Comprobando que la web responde...' -NoNewline
try { $resp = Invoke-WebRequest ($homeUrl + '/?nocache=' + $stamp) -UseBasicParsing -TimeoutSec 25
      Write-Host (' HTTP ' + [int]$resp.StatusCode) -ForegroundColor Green }
catch { Write-Host ' no respondio como se esperaba' -ForegroundColor Yellow; Write-Host $_.Exception.Message -ForegroundColor DarkGray }

Write-Host ''
Write-Host '=====================================================' -ForegroundColor Green
Write-Host ' PUBLICACION TERMINADA' -ForegroundColor Green
Write-Host "  Subidos $subidos / $($files.Count)  |  Verificados $okv / $($files.Count)"
Write-Host "  Si algo salio mal, tienes el backup en:  $backupDir"
Write-Host '=====================================================' -ForegroundColor Green
Write-Host ''
Read-Host 'Pulsa Enter para cerrar'
