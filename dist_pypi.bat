@echo off
rem Script will upload to the test account by default.
rem Pass first parameter as --help for usage

rem !*! Thanks dbenham for the bat script to regex the ini file; wow.  https://www.dostips.com/forum/viewtopic.php?f=3&t=6044

rem Do we need to show the help for usage of this tool?
set "para1=%~1"
rem don't pass %~1 directly as it's context changes between function scopes
call :argparse para1
if "%para1%"=="1" (
    rem we showed the help file, drop out of the script
    EXIT /B /0
)


rem Load variables from a file not checked-in to source control, like user name
call dist_pypi_config.bat

rem For readability, we'll build up the command using a series of variables.

rem While examples show uploading the dist\* directory, I prefer a specific filename to upload
rem Distribute the latest file, sorted on name,to pypi.  See https://ss64.com/nt/dir.html
for /f %%i in ('dir dist /b /O:D') do set dist_file="dist\%%i"
rem @echo %dist_file%

rem If no parameter upload to test.pypi.org
if ("%~1"=="--env") AND ("%~2"=="pypi") (
    set "env=https://pypi.org/legacy/"
) else (
    set "env=https://test.pypi.org/legacy/"
)

rem the caret (^) creates a multiple line string and must be the last character (do not put a space in front of it)
set cmd=venv_27\scripts\python.exe -m twine upload --verbose^
 --repository-url %env%^
 "%dist_file%"^
 --username "%user_name%"^
 --password "%password%"

rem @echo %cmd%
rem @echo:
echo Beginning submission to %env%  ...
echo File to upload: %dist_file%
call %cmd%
call :update_version

EXIT /B /0

rem Function argparse, to parse arguments from the command line
:argparse
rem if "%~1"=="/?" (
if "%para1%"=="/?" (
    call :usage
    set %~1=1
) else if "%para1%"=="-h" (
    call :usage
    set %~1=1
) else if "%para1%"=="--help" (
    set %~1=1
    call :usage
)

EXIT /B /0

rem Function usage to display how this utility runs, as a help switch
:usage
echo usage:   dist_pypi [--help] [--env test.pypi ^| pypi]
echo.
echo Distribute your latest file in dist\ folder to PyPI.  By default it will upload
echo to test.pypi.org to enforce the best practice of testing your distribution before
echo littering the main Python Package Index (PyPI).
echo.
echo optional arguments:
echo   --help   show this help message and exit
echo   --env    PyPI environment to use.  By default, with no arguments,
echo            will upload to test.pypi.org.
EXIT /B /0

rem Function update_version updates certain build number values in the configuration file
:update_version
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
rem remove 0 padding from the Month if present
if "%MM:~0,1%"=="0" (
    rem remove the 0 padding on the hour value
    set "M0=%MM:~1,2%"
) else (
    set "M0=%MM%"
)
rem remove 0 padding from the Day if present
if "%DD:~0,1%"=="0" (
    rem remove the 0 padding on the hour value
    set "D0=%DD:~1,2%"
) else (
    set "D0=%DD%"
)
rem remove 0 padding from the hour if present
if "%HH:~0,1%"=="0" (
    rem remove the 0 padding on the hour value
    set "H0=%HH:~1,2%"
) else (
    set "H0=%HH%"
)
rem Which variable to update?  Upload to pypi.org or test.pypi.org?
if "%env%"=="https://pypi.org/legacy/" (
    call jrepl "^publish_pypi = .*" "publish_pypi = %YYYY%.%M0%.%D0%.%HH%%Min%" /f browser_driver.cfg /o -
    echo Published to %env%. Updated configuration file publish_pypi = %YYYY%.%M0%.%D0%.%HH%%Min%
) else (
    call jrepl "^publish_test_pypi = .*" "publish_test_pypi = %YYYY%.%M0%.%D0%.%HH%%Min%" /f browser_driver.cfg /o -
    echo Published to %env%. Updated configuration file publish_test_pypi = %YYYY%.%M0%.%D0%.%HH%%Min%
)





rem https://stackoverflow.com/questions/18871870/batch-file-to-edit-an-ini
rem https://www.dostips.com/forum/viewtopic.php?f=3&t=6044
rem https://stackoverflow.com/questions/11037831/filename-timestamp-in-windows-cmd-batch-script