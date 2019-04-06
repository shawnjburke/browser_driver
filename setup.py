# Originally inspired from http://go.chriswarrick.com/entry_points


from setuptools import setup

setup(author='Shawn J Burke',
      author_email='pypi.python@teamburke.com',
      description='Browser Driver is a Wrapper for Selenium Web Automation',
      keywords="selenium test testing automation browser",
      # newline separates Description: header in PKG-INFO from readme content
      long_description='\n' + open('README.rst').read(),
      name='sjb.browser_driver',
      packages=['browser_driver'],
      project_urls={
        "Bug Tracker": "https://github.com/shawnjburke/py_guide/issues/",
        "Documentation": "https://shawnjburke.github.io/py_guide/",
        "Source Code": "https://github.com/shawnjburke/py_guide/",
      },
      url="https://github.com/shawnjburke/py_guide",
      version='2019.4.5.2155',

      # entry_points={
      #    'console_scripts': [ 'py_guide = py_guide.__main__:main' ]
      #  },
      )
