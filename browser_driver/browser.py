"""browser is the primary class for this Python package.  An instance of this class will wrap a browser driver for
IE, Edge, Chrome, Firefox, Phantom or other configured Selenium drivers.  This wrapper class allows us to insulate
browser changes.  If a browser does something to change the behavior of selenium, we can add code here to deal with it.
For instance a browser change once required us to scroll objects in to view to find them, where prior to the change
it did not."""

import logging
from selenium import webdriver


class WebBrowser():
    def __init__(self, browser="Chrome"):
        """Setup the class.  Add logging.  Create an instance of the selenium driver, for which this class is
        primarily a wrapper around."""
        self.log = logging.getLogger(__name__)

        # Create a browser instance to manipulate.  Be flexible in casing and terminology with the fall through
        #   logic for the browser indicated.  By default, use Chrome.
        if browser is None:
            self.driver = webdriver.Chrome()
            self.log.debug("Created instance of Chrome browser for testing.")
        elif browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
            self.log.debug("Created instance of Chrome browser for testing.")
        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
            self.log.debug("Created instance of FireFox browser for testing.")
        elif browser.lower() == "edge":
            self.driver = webdriver.Edge()
            self.log.debug("Created instance of Edge browser for testing.")
        elif browser.lower() == "phantomjs":
            self.driver = webdriver.PhantomJS()
            self.log.debug("Created instance of PhantomJS browser for testing.")
        elif browser.lower() == "internet explorer":
            self.driver = webdriver.Ie()
            self.log.debug("Created instance of Internet Explorer browser for testing.")
        elif browser.lower() == "ie":
            self.driver = webdriver.Ie()
            self.log.debug("Created instance of Internet Explorer browser for testing.")
        else:
            # If no browser is specified, first statement should handle.  This is fallback.  Maybe if browser=""
            self.driver = webdriver.Chrome()

    def find_element_by_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)

        return element

    def quit(self):
        """This is a wrapper method for the native Selenium functionality.  While a user could all
        WebBrowser.driver.quit() this design allows for additional code to be done in a uniform way across all tests
        code, and it is more intuitive than having to know this object contains another object called driver."""
        self.driver.quit()

    @property
    def url(self):
        """Return the current url in the browser."""
        return self.driver.current_url

    @url.setter
    def url(self, value):
        """Setting the URL will work as our navigate method in this class"""
        self.__url = value
        self.driver.get(value)

    @property
    def name(self):
        """This is a wrapper method for the native Selenium functionality.  While a user could all
        WebBrowser.driver.name this design allows for code to be done in a uniform way across all tests
        code, and it is more intuitive than having to know this object contains another object called driver."""

        return self.driver.name
