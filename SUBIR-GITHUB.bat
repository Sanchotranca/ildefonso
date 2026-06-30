@echo off
cd /d "%~dp0"
echo === Commit y push === > git-log.txt
git add .github/workflows/gh-pages.yml >> git-log.txt 2>&1
git commit -m "Add GitHub Pages Actions workflow" >> git-log.txt 2>&1
git remote remove origin >> git-log.txt 2>&1
git remote add origin https://github.com/Sanchotranca/ildefonso.git >> git-log.txt 2>&1
git push origin HEAD:main >> git-log.txt 2>&1
git push -f origin HEAD:claude/create-residencia-website-pP3AP >> git-log.txt 2>&1
echo Codigo de salida: %errorlevel% >> git-log.txt
echo Fin. >> git-log.txt
echo.
echo === LISTO ===
echo Ahora en GitHub ve a:
echo Settings - Pages - Source: GitHub Actions
echo https://github.com/Sanchotranca/ildefonso/settings/pages
pause
