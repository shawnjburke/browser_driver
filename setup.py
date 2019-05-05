# Originally inspired from http://go.chriswarrick.com/entry_points
# https://stackoverflow.com/questions/50585246/pip-install-creates-only-the-dist-info-not-the-package

from backports import configparser2
from datetime import datetime
from packaging import version
from setuptools import setup, find_packages


def version_builder(write_new_version=True):
    """This method determines the next version number.  The assumption is the version numbering scheme is relying on
    a timestamp based version, in contrast to Major.Minor.Revision type of structure.  THAT IS A NON-STANDARD SCHEME."""
    ini_file_name = "browser_driver.ini"
    now = datetime.now()

    ini_file = configparser2.ConfigParser()
    ini_file.read(ini_file_name)
    version_current = ini_file["browser_driver"]["version"]
    version_next = "{0}.{1}.{2}".format(str(now.year), str(now.month), str(now.day))
    # Is the version already set to to day?  If so, add in the time
    military_time = int(str(now.hour) + "{:02d}".format(now.minute))
    while version.parse(version_next) <= version.parse(version_current):
        version_next = "{0}.{1}.{2}.{3}".format(str(now.year), str(now.month), str(now.day), str(military_time))
        military_time += 1

    # Update the version number in the ini file
    if write_new_version:
        # Set the value in memory in the object
        ini_file["browser_driver"]["version"] = version_next
        # Write the file to disk using all the values of the object in memory
        with open('browser_driver.ini', 'w') as ini_disk_file:
            ini_file.write(ini_disk_file)

    return version_next


setup(author='Shawn J Burke',
      author_email='pypi.python@teamburke.com',
      classifiers=[
              # Trove classifiers
              # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
              'Development Status :: 4 - Beta',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: MIT License',
              'Natural Language :: English',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              # https://www.geeksforgeeks.org/difference-various-implementations-python/
              'Programming Language :: Python :: Implementation :: CPython',
              # Need to test to see if this will run on PyPy.  That'd be cool.
              # 'Programming Language :: Python :: Implementation :: PyPy',
              'Topic :: Software Development :: Quality Assurance',
              'Topic :: Software Development :: Testing'
            ],
      # data_files=[('', ['./browser_driver.ini'])],
      description='Browser Driver is a Wrapper for Selenium Web Automation',
      # entry_points={
      #    'console_scripts': [ 'py_guide = py_guide.__main__:main' ]
      #  },
      install_requires=[
          'docutils>=0.3',
          'selenium>=3.12.0'
      ],
      keywords="selenium test testing automation browser",
      license="MIT",
      # newline separates Description: header in PKG-INFO from readme content
      long_description='\n' + open('README.rst').read(),
      long_description_content_type='text/x-rst',
      name='sjb.browserdriver',
      # packages=['browser_driver'],
      packages=find_packages(),
      project_urls={
        "Bug Tracker": "https://github.com/shawnjburke/browser_driver/issues/",
        "Documentation": "https://shawnjburke.github.io/browser_driver/",
        "Source Code": "https://github.com/shawnjburke/browser_driver/",
      },
      test_suite="browser_driver.tests.browser_tests",
      url="https://github.com/shawnjburke/browser_driver",
      version=version_builder(write_new_version=True),
      )
