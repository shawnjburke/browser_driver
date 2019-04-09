# Originally inspired from http://go.chriswarrick.com/entry_points


from setuptools import setup, find_packages

setup(author='Shawn J Burke',
      author_email='pypi.python@teamburke.com',
      description='Browser Driver is a Wrapper for Selenium Web Automation',
      keywords="selenium test testing automation browser",
      # newline separates Description: header in PKG-INFO from readme content
      long_description='\n' + open('README.rst').read(),
      name='sjb.browser_driver',
      # packages=['browser_driver'],
      packages=find_packages("browser_driver"),
      project_urls={
        "Bug Tracker": "https://github.com/shawnjburke/browser_driver/issues/",
        "Documentation": "https://shawnjburke.github.io/browser_driver/",
        "Source Code": "https://github.com/shawnjburke/browser_driver/",
      },
      url="https://github.com/shawnjburke/browser_driver",
      version='2019.4.8-2135',

      # entry_points={
      #    'console_scripts': [ 'py_guide = py_guide.__main__:main' ]
      #  },
      )
