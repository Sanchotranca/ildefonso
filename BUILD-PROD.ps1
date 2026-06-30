# =========================================================================
# BUILD-PROD.ps1 — Genera versiones minificadas y prepara el sitio para deploy
# Residencia Universitaria San Ildefonso UAH — Estandar ELIAWEB v4
# =========================================================================
#
# Que hace:
#   1. Instala terser (JS) y clean-css-cli (CSS) localmente si no estan
#   2. Minifica css/style.css     -> css/style.min.css
#   3. Minifica js/main.js        -> js/main.min.js
#   4. Crea copia de seguridad de los HTML/PHP originales en .build-backup/
#   5. Reemplaza referencias 'css/style.css' por 'css/style.min.css'
#      y 'js/main.js' por 'js/main.min.js' en TODOS los HTML/PHP
#
# Como usar:
#   1. Abrir PowerShell en esta carpeta
#   2. Ejecutar: .\BUILD-PROD.ps1
#   3. Subir todo a FTP excepto la carpeta .build-backup/
#   4. Para volver a dev: .\BUILD-PROD.ps1 -Restore
#
# Pre-requisitos: Node.js + npm instalados (https://nodejs.org/)
# =========================================================================

param(
  [switch]$Restore
)

$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot
Set-Location $ProjectRoot

$BackupDir = Join-Path $ProjectRoot ".build-backup"
$HtmlFiles = @(
  "index.html","residencia.html","contacto.html","contacto.php",
  "habitaciones.html","servicios.html",
  "aviso-legal.html","politica-privacidad.html","politica-cookies.html",
  "gracias.html","404.html"
)

# ----- Modo restaurar -----
if ($Restore) {
  if (-not (Test-Path $BackupDir)) {
    Write-Host "No hay copia de seguridad en $BackupDir. Nada que restaurar." -ForegroundColor Yellow
    exit 0
  }
  Write-Host "Restaurando HTML/PHP desde $BackupDir..." -ForegroundColor Cyan
  foreach ($f in $HtmlFiles) {
    $src = Join-Path $BackupDir $f
    if (Test-Path $src) {
      Copy-Item $src $f -Force
      Write-Host "  restaurado $f"
    }
  }
  # Borrar los .min para evitar confusion
  Remove-Item "css/style.min.css" -ErrorAction SilentlyContinue
  Remove-Item "js/main.min.js"    -ErrorAction SilentlyContinue
  Write-Host "Restauracion completa. Las referencias vuelven a los originales." -ForegroundColor Green
  exit 0
}

# ----- Verificar node/npm -----
$nodeOk = $false
try { $null = node --version; $nodeOk = $true } catch { }
if (-not $nodeOk) {
  Write-Host "ERROR: Node.js no esta instalado. Descarga desde https://nodejs.org/" -ForegroundColor Red
  exit 1
}

# ----- Instalar herramientas si no estan -----
if (-not (Test-Path "node_modules/.bin/cleancss.cmd") -or -not (Test-Path "node_modules/.bin/terser.cmd")) {
  Write-Host "Instalando terser + clean-css-cli (solo la primera vez)..." -ForegroundColor Cyan
  if (-not (Test-Path "package.json")) {
    npm init -y | Out-Null
  }
  npm install --save-dev terser clean-css-cli 2>&1 | Out-Null
}

$cleancss = Join-Path $ProjectRoot "node_modules\.bin\cleancss.cmd"
$terser   = Join-Path $ProjectRoot "node_modules\.bin\terser.cmd"

# ----- Minificar CSS -----
Write-Host "Minificando css/style.css..." -ForegroundColor Cyan
& $cleancss --level 1 css/style.css -o css/style.min.css
$orig = (Get-Item css/style.css).Length
$min  = (Get-Item css/style.min.css).Length
$pct  = [math]::Round(100 - ($min / $orig * 100), 1)
Write-Host "  CSS: $orig -> $min bytes ($pct% menos)" -ForegroundColor Green

# ----- Minificar JS -----
Write-Host "Minificando js/main.js..." -ForegroundColor Cyan
& $terser js/main.js --compress --mangle -o js/main.min.js
$orig = (Get-Item js/main.js).Length
$min  = (Get-Item js/main.min.js).Length
$pct  = [math]::Round(100 - ($min / $orig * 100), 1)
Write-Host "  JS: $orig -> $min bytes ($pct% menos)" -ForegroundColor Green

# ----- Backup HTML/PHP originales -----
if (-not (Test-Path $BackupDir)) { New-Item -Path $BackupDir -ItemType Directory | Out-Null }
Write-Host "Copia de seguridad de HTML/PHP en $BackupDir/..." -ForegroundColor Cyan
foreach ($f in $HtmlFiles) {
  if (Test-Path $f) { Copy-Item $f (Join-Path $BackupDir $f) -Force }
}

# ----- Reemplazar referencias en HTML/PHP -----
Write-Host "Reemplazando referencias a .min en HTML/PHP..." -ForegroundColor Cyan
foreach ($f in $HtmlFiles) {
  if (-not (Test-Path $f)) { continue }
  $content = Get-Content $f -Raw -Encoding UTF8
  $content = $content -replace 'href="css/style\.css"',  'href="css/style.min.css"'
  $content = $content -replace 'src="js/main\.js"',       'src="js/main.min.js"'
  Set-Content $f $content -NoNewline -Encoding UTF8
  Write-Host "  $f"
}

Write-Host ""
Write-Host "BUILD COMPLETO." -ForegroundColor Green
Write-Host "  - CSS minificado: css/style.min.css"
Write-Host "  - JS minificado:  js/main.min.js"
Write-Host "  - HTML/PHP apuntan a las versiones .min"
Write-Host "  - Copia de seguridad en .build-backup/ (no subir al FTP)"
Write-Host ""
Write-Host "Para deshacer:  .\BUILD-PROD.ps1 -Restore" -ForegroundColor Yellow
