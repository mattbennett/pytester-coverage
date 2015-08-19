#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='app',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        "coverage",
        "pytest",
        "pytest-cov",
    ],
)
