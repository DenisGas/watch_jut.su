@echo off
set SCRIPT_NAME=main.py
set SHORTCUT_NAME=Watch_Jut.su.lnk
set ICON_FOLDER=ico

set WORKING_DIR=%CD%
set SCRIPT_PATH=%WORKING_DIR%\%SCRIPT_NAME%
set DESKTOP_PATH=%USERPROFILE%\Desktop
set ICON_PATH=%WORKING_DIR%\%ICON_FOLDER%\ico.ico
set SHORTCUT_PATH=%DESKTOP_PATH%\%SHORTCUT_NAME%

echo Creating shortcut...
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SHORTCUT_PATH%'); $s.TargetPath = '%SCRIPT_PATH%'; $s.IconLocation = '%ICON_PATH%'; $s.WorkingDirectory = '%WORKING_DIR%'; $s.Save()"

echo Shortcut created successfully!

