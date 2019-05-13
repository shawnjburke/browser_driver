==============================================
browser_driver
==============================================
This project contains a wrapper for selenium, a framework to automate a browser,
and often used in testing.   This wrapper provides

    # Logging, because good software has good logging

    # Browser Upgrade Protection; because as they race to out-do each other, the
      browser behaves differently with some updates

    # Selenium behavior supplementation; for instance, with an update, Chrome required
      an element to be scrolled into view or an error occurred.  Having a central wrapper
      allows for making that sort of update in one location

    # Screenshots, because if you want to run lights-out (not visible), you'll need a
      screenshot of what went wrong to fix it.

Installation
=============

.. code-block:: python

    c:\browser_test> venv\scripts\pip -install sjb.browserdriver

To upgrade an existing installation add the additional switch

.. code-block:: python

    c:\browser_test> venv\scripts\pip -install sjb.browserdriver --upgrade

Documentation
==============

This project is documented using Sphinx and reStructuredText, using a theme provided by Read the Docs.

Documentation can be found in several locations

* docs\ as html
* docs_source\ as reStructuredText source
* https://shawnjburke.github.io/browser_driver/
