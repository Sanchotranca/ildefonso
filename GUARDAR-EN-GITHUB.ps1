# ================================================================
#  GUARDAR-EN-GITHUB.ps1   (CAPA DE CONTENCION 2: respaldo)
#  Guarda un punto de restauracion en GitHub (rama master).
#  >>> NO toca la web publicada. <<<
# ================================================================
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

Write-Host ''
Write-Host '=====================================================' -ForegroundColor Cyan
Write-Host '  GUARDAR EN GITHUB  (respaldo - NO publica la web)  ' -ForegroundColor Cyan
Write-Host '=====================================================' -ForegroundColor Cyan
Write-Host "Carpeta: $PSScriptRoot"
Write-Host ''

# 0) git instalado?
try { git --version | Out-Null } catch {
    Write-Host 'ERROR: git no esta instalado en Windows.' -ForegroundColor Red
    Write-Host 'Instalalo desde https://git-scm.com/download/win y repite.'
    Read-Host 'Pulsa Enter para salir'; exit 1
}

# 0b) identidad para poder hacer commits (si falta, pone una local)
if (-not (git config user.email)) {
    git config user.email 'moody@localhost'
    git config user.name  'Moody'
    Write-Host 'Puesta identidad git local (Moody).' -ForegroundColor DarkGray
}

# 1) que hay para guardar
$cambios = git status --porcelain
if ([string]::IsNullOrWhiteSpace($cambios)) {
    Write-Host 'No hay cambios nuevos respecto al ultimo respaldo.' -ForegroundColor Yellow
    Write-Host 'Reviso si quedan commits sin subir...'
} else {
    Write-Host 'ESTO es lo que se va a guardar:' -ForegroundColor Green
    Write-Host ''
    git status --short
    Write-Host ''
    $r = Read-Host 'Escribe  SI  para guardarlo en GitHub  (cualquier otra tecla = cancelar)'
    if ($r -ne 'SI') {
        Write-Host 'CANCELADO. No se ha tocado nada.' -ForegroundColor Yellow
        Read-Host 'Pulsa Enter para salir'; exit 0
    }
    $msg = 'Respaldo ' + (Get-Date -Format 'yyyy-MM-dd HH:mm')
    git add -A
    git commit -m $msg | Out-Null
    Write-Host "Punto de restauracion creado: $msg" -ForegroundColor Green
}

# 2) subir a GitHub
Write-Host ''
Write-Host 'Subiendo a GitHub (rama master)...'
Write-Host '(Si pide login de GitHub, aceptalo.)'
git push origin master
if ($LASTEXITCODE -ne 0) {
    Write-Host ''
    Write-Host 'ERROR al subir a GitHub. Revisa tu conexion o tu login de GitHub.' -ForegroundColor Red
    Read-Host 'Pulsa Enter para salir'; exit 1
}

# 3) resumen
Write-Host ''
Write-Host 'LISTO. Respaldo guardado en GitHub.' -ForegroundColor Green
Write-Host ''
Write-Host 'Ultimos puntos de restauracion (puedes volver a cualquiera):'
git log --oneline -5
Write-Host ''
Write-Host '>>> La web publicada NO se ha tocado. <<<' -ForegroundColor Yellow
Write-Host ''
Read-Host 'Pulsa Enter para cerrar'
