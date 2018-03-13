#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="python-halftone",
      version="0.0.2",
      description="Create halftone variants of images",
      license="MIT",
      install_requires=["pillow==5.0.0"],
      author="philgyford, cybertoast",
      author_email="sundar@localprojects.com",
      url="https://github.com/local-projects/python-halftone",
      packages = find_packages(),
      keywords= "halftone",
      zip_safe = True
)
