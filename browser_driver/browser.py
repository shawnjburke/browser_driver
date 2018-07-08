"""browser is the primary class for this Python package.  An instance of this class will wrap a browser driver for
IE, Edge, Chrome, Firefox, Phantom or other configured Selenium drivers.  This wrapper class allows us to insulate
browser changes.  If a browser does something to change the behavior of selenium, we can add code here to deal with it.
For instance a browser change once required us to scroll objects in to view to find them, where prior to the change
it did not."""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class WebBrowser():
    def __init__(self, browser="Chrome"):
        """Setup the class.  Add logging.  Create an instance of the selenium driver, for which this class is
        primarily a wrapper around."""
        self.log = logging.getLogger(__name__)
        self.driver_timeout = 10

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

    def check_by_xpath(self, xpath):
        """Checks a checkbox, finding it by an xpath statement.  If not selected will click() the box.  Otherwise
        will leave the state unchanged.  This method does NOT toggle state of the checkbox.
        """
        element = self.find_element_clickable((by.XPATH, xpath))
        if not element.is_selected():
            element.click()

    def check_by_id(self, element_id):
        """Checks a checkbox, finding it by an html id value.  If not selected will click() the box.  Otherwise
        will leave the state unchanged.  This method does NOT toggle state of the checkbox.
        """
        element = self.find_element_clickable((by.ID, element_id))

        if not element.is_selected():
            # Check it
            element.click()

        return element

    def uncheck_by_id(self, element_id):
        """Removes check on a checkbox, finding it by an html id.  If selected will click() the box to deselect.
        Otherwise will leave the state unchanged.  This method does NOT toggle state of the checkbox.
        """
        element = self.find_element_clickable((by.ID, element_id))

        if element.is_selected():
            # Uncheck it
            if self.scroll_into_view(element):
                element.click()

    def uncheck_by_xpath(self, xpath):
        """Removes check on a checkbox, finding it by an xpath statement.  If selected will click() the box to deselect.
        Otherwise will leave the state unchanged.  This method does NOT toggle state of the checkbox.
        """
        element = self.find_element_clickable((by.XPATH, xpath))
        if element.is_selected():
            # Uncheck it
            if self.scroll_into_view(element):
                element.click()

    def find_element(self, locator):
        """Wrapper for finding an element using the wait technique.  This should help make the retrieval of the element
        more compatible with AJAX style web design.

            http://selenium-python.readthedocs.io/waits.html
        """
        try:
            element = WebDriverWait(self.driver, self.driver_timeout).until(
                ec.visibility_of_element_located(locator))

            return element
        except TimeoutException:
            self.log.error("The element was not found after {0}".format(self.driver_timeout))

    def find_element_clickable(self, locator):
        """Wrapper for finding if an element is clickable using the wait technique."""
        try:
            element = WebDriverWait(self.driver, self.driver_timeout).until(
                ec.element_to_be_clickable(locator))

            return element
        except TimeoutException:
            self.log.error("The element was not found after {0}".format(self.driver_timeout))

    def find_element_by_xpath(self, xpath):
        element = self.find_element((by.XPATH, xpath))

        return element

    def find_element_by_id(self, element_id):
        element = self.find_element((by.ID, element_id))

        return element

    def find_element_by_name(self, name):
        element = self.find_element((by.NAME, name))

        return element

    def scroll_into_view(self, element):
        # Let's bring it into view
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        element_in_view = True

        return element_in_view

    def quit(self):
        """This is a wrapper method for the native Selenium functionality.  While a user could all
        WebBrowser.driver.quit() this design allows for additional code to be done in a uniform way across all tests
        code, and it is more intuitive than having to know this object contains another object called driver."""
        self.driver.quit()

    @property
    def ip_port(self):
        return self.driver.command_executor._conn.port

    @property
    def host(self):
        return self.driver.command_executor._conn.host

    @property
    def url(self):
        """Return the current url in the browser."""
        return self.driver.current_url

    @url.setter
    def url(self, value):
        """Setting the URL will work as our navigate method in this class"""
        self._url = value
        self.driver.get(value)

    @property
    def name(self):
        """This is a wrapper method for the native Selenium functionality.  While a user could all
        WebBrowser.driver.name this design allows for code to be done in a uniform way across all tests
        code, and it is more intuitive than having to know this object contains another object called driver."""

        return self.driver.name
