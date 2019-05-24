==============================================
Release History for browser_driver
==============================================


v0.1.3
########

Bug fix where the setup process would update the cfg file key = value where the bat file was
updating as key=value.  Set bat file to key = value logic.

v0.1.2
########

Bug fix in dist_pypi.bat+browser_driver.cfg where key = value (with space) broke the update of distribution
date in file.  The file need to have key=value without spaces.

v0.1.1
########

Updated setup.py adding find_and_list_packages() method.  Updated the dist_pypi.bat script in a number of ways.
Including updating the date we uploaded to a pypi environment in the project cfg file.

v0.1.0
########

First development release to test.pypi.org with Semantic Version number scheme.  Up until this time
we had been messing with the idea of a calendar version.  This was abandoned because Semantic Version
is well know, and has value in what it communicates in it's MAJOR.MINOR.REVISION schema, including
indicating a breaking of the public api, when the MAJOR portion is changed.
