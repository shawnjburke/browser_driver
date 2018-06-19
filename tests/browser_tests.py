import unittest2
from browser_driver import browser


class BrowserDriverTests(unittest2.TestCase):
    def setUp(self):
        self.driver = browser.WebBrowser()

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
            self.driver.quit()
        else:
            print("WARNING: Errors observed in execution of {0}().".format(self._testMethodName))
            if self.driver.name is not "phantomjs":
                print("Did not call driver.quit() leaving {0} browser open for debugging.".format(self.driver.name))
            else:
                self.driver.quit()

    def test_browser_default(self):
        """Test that no specified browser name causes Chrome to be invoked"""
        self.assertIsNotNone(self.driver)
        self.assertEqual(self.driver.name.lower(), "chrome")

    def test_browser_Firefox(self):
        """Test that a Firefox browser can be used.  Test the name is not case sensitive."""
        self.driver = browser.WebBrowser("FireFOX")
        self.assertIsNotNone(self.driver)
        self.assertEqual(self.driver.name.lower(), "firefox")

    def test_navigate(self):
        """Tests that the browser navigates to a page."""
        url = "https://www.google.com/"
        self.driver.url = url
        self.assertEqual(url, self.driver.url)
        element = self.driver.find_element_by_xpath('//*[@id="hplogo"]')
        self.assertIsNotNone(element)
