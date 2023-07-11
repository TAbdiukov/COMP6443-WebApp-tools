#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="courseDB_patch",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask-core"],
    package_data={"courseDB_patch": ["templates/*/*", "assets/static/*/*"]},
)
