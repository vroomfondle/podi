#!/usr/bin/env python3
"""
    Podi, a command-line interface for Kodi.
    Copyright (C) 2015  Peter Frost <slimeypete@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from setuptools import setup, find_packages

setup(
    name="Podi",
    version="0.1",
    author="Peter Frost",
    author_email="slimeypete@gmail.com"
    packages=find_packages(),
    install_requires=[
        "cement >= 2.4.0", "pystache >= 0.5.4", "pyyaml >= 3.11", ],
    test_require=["nose >= 1.3.7"],
    scripts=["./podi.py"],
    package_data={"app.view": "*.m"}

)
