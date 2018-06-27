# Originally inspired from http://go.chriswarrick.com/entry_points


from setuptools import setup

setup(author='Shawn J Burke',
      author_email='shawn.burke@teamburke.com',
      description='Browser Driver is a Wrapper for Selenium Web Automation',
      long_description=open('README.rst').read(),
      name='sjb.browser_driver',
      version='0.1.0',
      packages=['browser_driver'],
      entry_points={
          'console_scripts': [ 'py_guide = py_guide.__main__:main' ]
        },
      )
