#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Setup script for django_dkim."""
import os

from setuptools import find_packages, setup

import django_dkim


def readme():
    """Return content of README file."""
    with open(os.path.join(os.path.dirname(__file__), "README.rst")) as f:
        return f.read()


INSTALL_REQUIRES = ["Django>=3.2", "dkimpy", "future"]
EXTRAS_REQUIRE = {"quality": ["flake8", "isort", "pydocstyle"], "test": ["mock"]}

setup(
    name="django-dkim",
    version=django_dkim.__version__,
    description="DKIM signing e-mail backend for Django",
    long_description=readme(),
    url="https://gitlab.com/stinovlas/django-dkim",
    author="Jan Musílek",
    author_email="stinovlas@gmail.com",
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.8, <4",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
