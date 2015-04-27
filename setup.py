#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
  name = "Podi",
  version = "0.1",
  packages = find_packages(),
  install_requires = ["cement >= 2.4.0", "pystache >= 0.5.4", "pyyaml >= 3.11",],
  test_require = ["nose >= 1.3.7"],
  scripts = ["./podi.py"],
  package_data = {"app.view": "*.m"}

)
