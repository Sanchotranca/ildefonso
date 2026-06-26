@echo off
cd /d "%~dp0"
echo === REINICIO COMPLETO === > git-log.txt

echo Borrando historial git... >> git-log.txt
rmdir /s /q .git >> git-log.txt 2>&1

echo Inicializando git limpio... >> git-log.txt
git init >> git-log.txt 2>&1
git config user.email "sanildefonso@crusa.es" >> git-log.txt 2>&1
git config user.name "Residencia San Ildefonso" >> git-log.txt 2>&1

echo Añadiendo todos los archivos... >> git-log.txt
git add -A >> git-log.txt 2>&1
git commit -m "Sitio web Hotel Residencia San Ildefonso - contenido real" >> git-log.txt 2>&1

echo Conectando con GitHub... >> git-log.txt
git remote add origin https://github.com/Sanchotranca/ildefonso.git >> git-log.txt 2>&1

echo Subiendo a GitHub... >> git-log.txt
git push -f origin HEAD:main >> git-log.txt 2>&1
git push -f origin HEAD:gh-pages >> git-log.txt 2>&1

echo Codigo de salida: %errorlevel% >> git-log.txt
echo Fin. >> git-log.txt

echo.
echo === LISTO ===
echo Espera 60 segundos y abre:
echo https://sanchotranca.github.io/ildefonso/
pause
