rem Current Path
set CURPATH=%cd%

rem Anaconda Environment
set root=C:\ProgramData\Anaconda3
call %root%\Scripts\activate.bat %root%

rem Execute
call cd %CURPATH%
call python cartoon.py

pause