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
Currently there is no installer for this package.  There is a setup.py file which can create the build.  If using
PyCharm there is a run configuration in the .idea\\runConfigurations directory.

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

..  seealso::

    `ChromeDriver Methods`_

..  _ChromeDriver Methods: https://seleniumhq.github.io/selenium/docs/api/dotnet/html/Methods_T_OpenQA_Selenium_Chrome_ChromeDriver.htm#mainBody