#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
from setup_utils import read, read_markdown

PACKAGE_NAME = "django-rest-framework-expandable"
PACKAGE_ROOT_NAME = "rest_framework_expandable"
GITHUB_URL = "https://github.com/alexseitsinger/{}".format(PACKAGE_NAME)
HOMEPAGE_URL = GITHUB_URL
README_NAME = "README.md"
INSTALL_REQUIRES = ["Django", "djangorestframework", "django_rest_framework_helpers"]
KEYWORDS = ["django", "rest", "djangorestframework"]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System",
]

setup(
    name=PACKAGE_NAME,
    version=read(("src", PACKAGE_ROOT_NAME, "__init__.py"), "__version__"),
    description=read_markdown((README_NAME,), "Description", (0,)),
    long_description=read((README_NAME,)),
    long_description_content_type="text/markdown",
    author="Alex Seitsinger",
    author_email="software@alexseitsinger.com",
    url=HOMEPAGE_URL,
    install_required=INSTALL_REQUIRES,
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["tests"]),
    include_package_data=True,
    license="BSD 2-Clause License",
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    project_urls={
        "Documentation": HOMEPAGE_URL,
        "Source": GITHUB_URL,
        "Tracker": "{}/issues".format(GITHUB_URL),
    },
)
