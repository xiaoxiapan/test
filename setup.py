from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30640",
      url="",
      author="Pan Xiaoxia",
      author_email="xiaoxia.pan@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_point={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
      )

