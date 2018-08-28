#!/usr/bin/env python
# file: setup.py
# author: mbiokyled29
import sys
from setuptools import setup

try:
    with open("requirements.txt") as reqs:
        lines = reqs.read().split("\n")
        requirements = list(filter(lambda l: not l.startswith("#"), lines))
except IOError:
    requirements = []

try:
    with open("requirements_dev.txt") as test_reqs:
        lines = test_reqs.read().split("\n")
        test_requirements = list(filter(lambda l: not l.startswith("#"), lines))
except IOError:
    test_requirements = []


setup(
    name="perfi",
    version="0.1.0",
    description="CLI tool to compute personal finance plans",
    author="Kyle McChesney",
    author_email="mbiokyle29@gmail.com",
    url="https://github.com/mbiokyle29/perfi",
    packages=["perfi", "perfi.lib", "perfi.lib.liability", "perfi.lib.asset"],
    package_dir={
        "perfi": "perfi",
        "perfi.lib": "perfi/lib",
        "perfi.lib.liability": "perfi/lib/liability",
        "perfi.lib.asset": "perfi/lib/asset",
    },
    entry_points="""
        [console_scripts]
        perfi=perfi.main:cli
    """,
    install_requires=requirements,
    zip_safe=False,
    keywords="perfi",
    classifiers=[],
    test_suite="tests",
    tests_require=test_requirements
)
