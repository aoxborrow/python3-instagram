#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="python3-instagram",
      version="0.9.0",
      description="Instagram API client",
      license="MIT",
      install_requires=["simplejson","httplib2"],
      author="Instagram, Inc",
      author_email="apidevelopers@instagram.com",
      url="http://github.com/paste/python3-instagram",
      packages = find_packages(),
      keywords= "instagram",
      zip_safe = True)
