Set-Location $PSScriptRoot
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Servidor local - Residencia Ildefonso" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Iniciando en: http://localhost:8080" -ForegroundColor Green
Write-Host "Para detener: Ctrl+C o cierra esta ventana" -ForegroundColor Yellow
Write-Host ""
Start-Process "http://localhost:8080"
python -m http.server 8080
