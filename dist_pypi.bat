@echo off
rem Script will upload to the test account by default.
rem To upload to pypi, not test, then pass the first parameter as pypi
rem https://stackoverflow.com/questions/26551/how-can-i-pass-arguments-to-a-batch-file
rem https://stackoverflow.com/questions/382587/how-to-get-batch-file-parameters-from-nth-position-on

rem set "dist_file=dist/sjb.browser_driver-2019.4.8.2135-py2-none-any.whl"
set "dist_file=dist/sjb.browser_driver-2019.4.14-py2-none-any.whl"

rem If no parameter upload to test.pypi.org
if "%~1"=="" (
    echo "Uploading to https://test.pypi.org/legacy/  ..."
    rem venv_27\scripts\python.exe -m twine upload --repository-url https://test.pypi.org/legacy/ dist/sjb.browser_driver-2019.4.8.2135-py2-none-any.whl
    set "env=https://test.pypi.org/legacy/"
) else (
    echo "Implement pypi production"
)

call venv_27\scripts\python.exe -m twine upload --repository-url %env% %dist_file%