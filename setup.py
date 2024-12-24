#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : setup.py
#
#       Creation Date : Wed 24 Jun 2020 06:46:12 PM EEST (18:46)
#
#       Last Modified : Wed 24 Jun 2020 08:30:44 PM EEST (20:30)
#
# ==============================================================================

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-letsmaintain",
    version="1.0.4",
    python_requires=">=3.9",
    description=(
        "Django middleware that provides a maintenance countdown warning message."
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/raratiru/django-letsmaintain",
    author="George Tantiras",
    license="BSD 3-Clause License",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["Django>=3.2"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Framework :: Django :: 5.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)
