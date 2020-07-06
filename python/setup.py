#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='hassh',
    version='1.0.0',
    description='HASSH is a method for creating SSH Client and Server fingerprints.',
    url="https://github.com/salesforce/hassh",
    author="Tommy Stallings",
    author_email="tommy.stallings@salesforce.com",
    maintainer = "John B. Althouse",
    maintainer_email = "jalthouse@salesforce.com",
    license="BSD",
    scripts=['hassh.py'],
    install_requires=['pyshark>=0.4.1']
)


