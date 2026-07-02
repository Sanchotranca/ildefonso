@echo off
REM CONTENCION - Publicar la web por FTPS (PowerShell puro, sin WinSCP).
REM Hace backup del sitio en vivo, ensena vista previa, pide PUBLICAR y verifica.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0PUBLICAR-WEB.ps1"
pause
