====================
About browser_driver
====================

This documentation is also hosted at

* https://shawnjburke.github.io/browser_driver/

This class wraps functionality provided by the Selenium peeps.  Created this class to do things like provide logging,
and handle quirks in browser behavior.  For instance it's not uncommon for a browser+browser-driver+python combination
to cause an issue.  For instance

    * elements need to be scrolled into view to be seen
    * Firefox (a browser) requires changing how the object is invoked

In addition to logging, wrapping also provides additional handling.  For instance when navigating to a new page we may
want to check the new page is loaded, before returning from the method, to avoid subsequent code from operating on a
stale page.