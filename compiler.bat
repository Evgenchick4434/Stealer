@echo off

set /p file="File name for compilation (for example test.py): "
set /p compression="Compress the file? (y/n): "
set /p console="Disable console? (y/n): "

@echo on

pip install virtualenv & virtualenv venv & call venv\Scripts\activate
pip install Nuitka

if "%compression%" == "y" (
    pip install zstandard
) else (
    echo Y|pip uninstall zstandard
)

if "%console%" == "y" (
    nuitka --onefile --plugin-enable=multiprocessing --windows-disable-console %file%
) else (
    nuitka --onefile --plugin-enable=multiprocessing %file%
)

pause