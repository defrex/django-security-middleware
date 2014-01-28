#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup, find_packages
import re


with open('security_middleware/__init__.py', 'r') as init_file:
    version = re.search(
        '^__version__ = [\'"]([^\'"]+)[\'"]',
        init_file.read(),
        re.MULTILINE,
    ).group(1)


setup(
    name='django-security-middleware',
    description='Some middleware for security',
    url='http://github.com/defrex/django-security-middleware/',
    license='BSD',
    author='Aron Jones',
    author_email='aron.jones@gmail.com',
    packages=find_packages(),
    version=version,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.6',
    ],
)
