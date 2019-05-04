==============================================
browser_driver
==============================================
This project contains a wrapper for selenium.  The wrapper deals with things such as
scrolling an item into view before clicking it.  In general, the wrapper helps
deal with changes in browsers for many reasons, including changes
between versions of the browser.

##############
Install
##############

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
    element = web.find_element_by_id("resultStats")
    web.assertIsNotNone(element, "Did not find results statistics element on page.")

##############
Documentation
##############
https://shawnjburke.github.io/browser_driver/

This class wraps functionality provided by the Selenium peeps.  Created this class to do things like provide logging,
and handle quirks in browser behavior.  For instance it's not uncommon for a browser+browser-driver+python combination
to cause an issue.  For instance

    * elements need to be scrolled into view to be seen
    * Firefox (a browser) requires changing how the object is invoked

In addition to logging, wrapping also provides additional handling.  For instance when navigating to a new page we may
want to check the new page is loaded, before returning from the method, to avoid subsequent code from operating on a
stale page.
