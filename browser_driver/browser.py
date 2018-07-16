"""browser is the primary class for this Python package.  An instance of this class will wrap a browser driver for
IE, Edge, Chrome, Firefox, Phantom or other configured Selenium drivers.  This wrapper class allows us to insulate
browser changes.  If a browser does something to change the behavior of selenium, we can add code here to deal with it.
For instance a browser change once required us to scroll objects in to view to find them, where prior to the change
it did not."""

import logging
import random
from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class WebBrowser:
    _url = None  # type: str

    def __init__(self, browser=None, logger=None):
        """Setup the class.  Add logging.  Create an instance of the selenium driver, for which this class is
        primarily a wrapper around.

        Property logger originally added because an expected hierarchy was not established when running from
        UnitTest2.TestCase.

        """
        if logger is None:
            self.log = logging.getLogger(__name__)
        else:
            # self.log = logger
            self.log = logging.getLogger("{0}.{1}".format(logger.name, __name__))

        self.log.debug("Logger {0} obtained for usage by {1}".format(self.log.name, self.name))
        self.driver_timeout = 10

        # If not specified, choose from installed browsers
        if browser is None:
            browser = "random"
        self.driver = self.browser_factory(browser)

    def browser_factory(self, browser):
        """This method will return a selenium driver object to manipulate the browser.  The method can provide a pseudo
        random creation of standard, visible, browsers."""

        # Limit the random choice of browser to what is known to be installed and visible
        random_browser_list = ['chrome', 'firefox']
        if browser.lower() == "random":
            browser = random.choice(random_browser_list)

        # Create a browser instance to manipulate.  Be flexible in casing and terminology with the fall through
        #   logic for the browser indicated.  By default, use Chrome.
        if browser is None:
            driver = webdriver.Chrome()
            self.log.debug("Created instance of Chrome browser for testing.")
        elif browser.lower() == "chrome":
            driver = webdriver.Chrome()
            self.log.debug("Created instance of Chrome browser for testing.")
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox()
            self.log.debug("Created instance of FireFox browser for testing.")
        elif browser.lower() == "edge":
            driver = webdriver.Edge()
            self.log.debug("Created instance of Edge browser for testing.")
        elif browser.lower() == "phantomjs":
            driver = webdriver.PhantomJS()
            self.log.debug("Created instance of PhantomJS browser for testing.")
        elif browser.lower() == "internet explorer":
            driver = webdriver.Ie()
            self.log.debug("Created instance of Internet Explorer browser for testing.")
        elif browser.lower() == "ie":
            driver = webdriver.Ie()
            self.log.debug("Created instance of Internet Explorer browser for testing.")
        else:
            # If no browser is specified, first statement should handle.  This is fallback.  Maybe if browser=""
            driver = webdriver.Chrome()
            self.log.debug("No browser name specified. Created instance of {0} browser for testing." \
                           .format(browser.name))

        return driver

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

    @contextmanager
    def click_to_new_page(self, element):
        """This is a wrapper for clicking an HTML hyperlink.  This method is specific to clicking a non-javascript link
        that loads a new page.  The method adds functionality to wait for the new page to load before retruning.  this
        addresses a common challenge.

        Thanks to http://www.obeythetestinggoat.com/how-to-get-selenium-to-wait-for-page-load-after-a-click.html
        """
        element.click()
        page_leaving = self.find_element_by_tag_name("html")
        yield
        WebDriverWait(self, self.driver_timeout).until(ec.staleness_of(page_leaving))

    def click_to_new_page_by_id(self, html_id):
        """This method finds an element by id, clicks it, and waits for the new page to load before returning."""
        element = self.find_element_by_id(html_id)

        self.click_to_new_page(element)

        return element

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
            msg = "A search by {0}, for element with {0}={1}, timed out after {2} seconds" \
                .format(locator[0], locator[1], self.driver_timeout)
            self.log.error(msg)

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

    def find_element_by_link_text(self, link_text):
        element = self.find_element((by.LINK_TEXT, link_text))

        return element

    def find_element_by_partial_link_text(self, partial_link_text):
        """Partial Link Text is case sensitive"""
        element = self.find_element((by.PARTIAL_LINK_TEXT, partial_link_text))

        return element

    def find_element_by_tag_name(self, tag_name):
        element = self.find_element((by.TAG_NAME, tag_name))

        return element

    def scroll_into_view(self, element):
        # Let's bring it into view
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        element_in_view = True

        return element_in_view

    def send_keys(self, element, keys_to_type):
        """When passed an element found to be clickable, will calls the send keys method to type the passed string in
        the textbox."""
        element.send_keys(keys_to_type)

        return element

    def send_keys_by_id(self, element_id, keys_to_type):
        element = self.find_element_clickable((by.ID, element_id))
        self.send_keys(element, keys_to_type)

        return element

    def send_keys_by_name(self, element_name, keys_to_type):
        element = self.find_element_clickable((by.NAME, element_name))
        self.send_keys(element, keys_to_type)

        return element

    def send_keys_by_xpath(self, element_xpath, keys_to_type):
        element = self.find_element_clickable((by.XPATH, element_xpath))
        self.send_keys(element, keys_to_type)

        return element

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

        # before the driver is established the logger will attempt to access a name.
        try:
            return self.driver.name
        except AttributeError:
            return __name__

