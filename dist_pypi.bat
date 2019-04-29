@echo off
rem Script will upload to the test account by default.
rem To upload to pypi, not test, then pass the first parameter as pypi
rem https://stackoverflow.com/questions/26551/how-can-i-pass-arguments-to-a-batch-file
rem https://stackoverflow.com/questions/382587/how-to-get-batch-file-parameters-from-nth-position-on

rem Load variables from a file not checked-in to source control, like user name
call dist_pypi_config.bat

rem For readability, we'll build up the command using a series of variables.

rem While examples show uploading the dist\* directory, I prefer a specific filename to upload
set "dist_file=dist/sjb.browserdriver-2019.4.28.1835-py2-none-any.whl"

rem If no parameter upload to test.pypi.org
if "%~1"=="pypi" (
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

rem call venv_27\scripts\python.exe -m twine upload --verbose --repository-url %env% "%dist_file%" --username "%user_name%" --password "%password%"
@echo %cmd%
@echo:
@echo Beginning submission to %env%  ...
call %cmd%