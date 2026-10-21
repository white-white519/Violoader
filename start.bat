@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo === Проверка синтаксиса ===
python -c "import ast; ast.parse(open('violoader.py', encoding='utf-8').read()); print('OK')"
if errorlevel 1 (
    echo.
    echo [ОШИБКА] Синтаксис violoader.py сломан. Смотри ошибку выше.
    pause
    exit /b 1
)

echo.
echo === Запуск violoader ===
python violoader.py

pause