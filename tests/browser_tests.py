import unittest2
import os
from browser_driver import browser


class BrowserDriverTests(unittest2.TestCase):
    def setUp(self):
        self.browser = browser.WebBrowser()

    def tearDown(self):
        """A set of actions to be used by all unittest2.TestCase.tearDown() methods.
            Args:
                test_case is an instance of unittest2.TestCase

            Example:
                class myTests(unitests2.TestCase):
                    tearDown(self):
                        helper_selenium_functions.py.tear_down(self)
        """
        if self._outcome.errors[1][1] is None:
            print("{0}() completed successfully and no errors were observed.".format(self._testMethodName))
            self.browser.quit()
        else:
            print("WARNING: Errors observed in execution of {0}().".format(self._testMethodName))
            if self.browser.name is not "phantomjs":
                print("Did not call driver.quit() leaving {0} browser open for debugging.".format(self.browser.name))
            else:
                self.browser.quit()

    def test_browser_default(self):
        """Test that no specified browser name causes Chrome to be invoked"""
        self.assertIsNotNone(self.browser)
        self.assertEqual(self.browser.name.lower(), "chrome")

    def test_browser_Firefox(self):
        """Test that a Firefox browser can be used.  Test the name is not case sensitive."""
        self.browser = browser.WebBrowser("FireFOX")
        self.assertIsNotNone(self.browser)
        self.assertEqual(self.browser.name.lower(), "firefox")

    def test_navigate(self):
        """Tests that the browser navigates to a page."""
        url = "https://www.google.com/"
        self.browser.url = url
        self.assertEqual(url, self.browser.url)

    def test_find_element_by_xpath(self):
        """Tests that the browser can find an element using an xPath statement."""
        url = "https://www.google.com/"
        self.browser.url = url
        element = self.browser.find_element_by_xpath('//*[@id="hplogo"]')
        self.assertIsNotNone(element)

    def test_find_element_by_id(self):
        """Tests that the browser can find an element using an id value."""
        url = "https://www.google.com/"
        self.browser.url = url
        element = self.browser.find_element_by_id("hplogo")
        self.assertIsNotNone(element)

    def test_checkboxes(self):
        """Ensures checking a box, unchecking it, and toggling the state work as expected."""
        url = "https://mdn.mozillademos.org/en-US/docs/Web/HTML/Element/input/checkbox$samples/Value?revision=1389331"
        self.browser.url = url
        element_id = "subscribeNews"
        element = self.browser.find_element_by_id(element_id)
        # Verify it's unchecked
        self.assertFalse(element.is_selected())
        # Check the box
        self.browser.check_by_id(element_id)
        self.assertTrue(element.is_selected())
        # Make sure check method is not toggling
        self.browser.check_by_id(element_id)
        self.assertTrue(element.is_selected())
        # Uncheck
        self.browser.uncheck_by_id(element_id)
        self.assertFalse(element.is_selected())
        # Make sure check method is not toggling
        self.browser.uncheck_by_id(element_id)
        self.assertFalse(element.is_selected())

    def test_click_not_in_view(self):
        """This test ensure the box can be clicked even if it is not initially in the viewable
        screen area"""
        url = "file://{0}/test_html.html".format(os.getcwd())
        url.replace('\\', '/')
        self.browser = browser.WebBrowser("Firefox")
        self.browser.url = url
        element = self.browser.check_by_id("horns")
        self.assertTrue(element.is_selected())
