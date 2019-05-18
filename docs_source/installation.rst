=========
Install
=========

.. code-block:: python

    c:\browser_test> venv\scripts\pip -install sjb.browserdriver

To upgrade an existing installation add the additional switch

.. code-block:: python

    c:\browser_test> venv\scripts\pip -install sjb.browserdriver --upgrade

If you want to build the project, and are using PyCharm (and if not, why?), there is a run configuration
in the .idea\\runConfigurations directory.

################
The Hello World
################

.. code-block:: python

    import logging
    import logging.handlers
    import os

    from browser_driver import browser

    # Get the top level application logger
    log = logging.getLogger(__name__)
    file_path = r"{0}".format(os.getcwd())
    file_name = "{0}\\browser_driver.log".format(file_path)
    file_log = logging.handlers.TimedRotatingFileHandler(filename=file_name,
                                                         when="D", interval=1, backupCount=30)
    file_log = logging.FileHandler(filename="{0}\\browser_driver.log".format(file_path))
    file_log.setFormatter(logging.Formatter(fmt="%(asctime)s | %(levelname)s | %(message)s"))
    file_log.setLevel(logging.DEBUG)

    # Using logging to populate standard output with info level log entries
    stdout_log = logging.StreamHandler(sys.stdout)
    stdout_log.setFormatter(logging.Formatter(fmt=""))
    stdout_log.setLevel(logging.INFO)

    log.addHandler(stdout_log)
    log.addHandler(file_log)
    log.setLevel(logging.DEBUG)

    web = browser.WebBrowser(logger=log)
    web.url = "https://www.google.com"
    web.send_keys_by_name('q', 'pypi browserdriver')
    xpath = r'//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]'
    web.click_element_by_xpath(xpath)
