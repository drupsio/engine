import os
import re

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_requirements(filename):
    return open("requirements/" + filename).read().splitlines()


def get_package_version():
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
    description="Engine for Drups.io ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drupsio/engine",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.6",
    install_requires=get_requirements("default.txt"),
)
