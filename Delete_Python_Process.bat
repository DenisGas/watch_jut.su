@echo off

REM Specify the name of the process to be terminated
set PROCESS_NAME=chromedriver.exe

REM Terminate the process
taskkill /F /IM %PROCESS_NAME%

echo Process %PROCESS_NAME% terminated successfully!
