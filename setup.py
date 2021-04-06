"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, March 2021
"""

import os
import re

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_requirements(filename):
    """
    Get requirements file content by filename.

    :param filename: Name of requirements file.
    :return: Content of requirements file.
    """

    return open("requirements/" + filename).read().splitlines()


def get_package_version():
    """
    Read the version of drups module without importing it.

    :return: The version
    """

    version = re.compile(r"VERSION\s*=\s*\((.*?)\)")
    base = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base, "drups/__init__.py")) as file:
        for line in file:
            match = version.match(line.strip())
            if not match:
                continue
            return ".".join(match.groups()[0].split(", "))


setup(
    name="drups",
    version=get_package_version(),
    author="Temuri Takalandze",
    author_email="temo@drups.io",
    description="Engine for Drups.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drupsio/engine",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.6",
    install_requires=get_requirements("default.txt"),
    test_suite="tests",
    tests_require=get_requirements("test.txt"),
    entry_points={
        "console_scripts": [
            "drups = drups.__main__:main",
        ]
    },
)
