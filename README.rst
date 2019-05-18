==============================================
browser_driver
==============================================
This project contains a wrapper for selenium, a framework to automate a browser,
and often used in testing.   This wrapper provides

    1. Logging, because good software has good logging

    2. Browser Upgrade Protection; because as they race to out-do each other, the
       browser behaves differently with some updates

    3. Selenium behavior supplementation; for instance, with an update, Chrome required
       an element to be scrolled into view or an error occurred.  Having a central wrapper
       allows for making that sort of update in one location

    4. Screenshots, because if you want to run lights-out (not visible), you'll need a
       screenshot of what went wrong to fix it.

Installation
=============

.. code-block:: python

    c:\browser_test> venv\scripts\pip -install sjb.browserdriver

To upgrade an existing installation add the additional switch

.. code-block:: python

    c:\browser_test> venv\scripts\pip -install sjb.browserdriver --upgrade

Recent Changes
==============

The full change log can be found at [TODO: update with link]

v0.1.3 - Bug fix where the setup process would update the cfg file key = value where the bat file was
updating as key=value.

v0.1.2 - Bug fix in dist_pypi.bat+browser_driver.cfg

v0.1.1 - Updated setup.py adding find_and_list_packages() method.  Updated the dist_pypi.bat script in a number of ways.
Including updating the date we uploaded to a pypi environment in the project cfg file.

v0.1.0 - First development release to test.pypi.org with Semantic Version number scheme.


Documentation
==============

This project is documented using Sphinx and reStructuredText, using a theme provided by Read the Docs.

Documentation can be found in several locations

* docs\\ as html
* docs_source\\ as reStructuredText source
* https://shawnjburke.github.io/browser_driver/
