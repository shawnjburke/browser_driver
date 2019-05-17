@echo off
rem Script will upload to the test account by default.
rem To upload to pypi, not test, then pass the first parameter as pypi
rem https://stackoverflow.com/questions/26551/how-can-i-pass-arguments-to-a-batch-file
rem https://stackoverflow.com/questions/382587/how-to-get-batch-file-parameters-from-nth-position-on


rem Do we need to show the help for usage of this tool?
if "%~1"=="/?" (
    call :usage
    EXIT /B /0
) else if "%~1"=="-h" (
    call :usage
    EXIT /B /0
) else if "%~1"=="--help" (
    call :usage
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
if ("%~1"=="--env") AND ("%~1"=="pypi") (
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

EXIT /B /0

:usage

echo usage:   dist_pypi [--help] [--env test.pypi ^| pypi]
echo.
echo Distribute your latest file in dist\ folder to PyPI.  By default it will upload
echo to test.pypi.org to enforce the best practice of testing your distribution before
echo littering the main Python Package Index (PyPI).
echo.
echo optional arguments:
echo   --help   show this help message and exit
echo   --env    PyPI environment to use.  By default, or with no arguments
echo            will upload to test.pypi.org.

EXIT /B /0
