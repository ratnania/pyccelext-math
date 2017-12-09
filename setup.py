# -*- coding: UTF-8 -*-
#! /usr/bin/python

import sys
from setuptools import setup, find_packages
import pyccelext_math

NAME    = 'pyccelext_math'
VERSION = pyccelext_math.__version__
AUTHOR  = 'Ahmed Ratnani'
EMAIL   = 'ahmed.ratnani@ipp.mpg.de'
URL     = 'https://github.com/pyccel/pyccelext-math'
DESCR   = 'Pyccel extension for Linear Algebra.'
KEYWORDS = ['math']
LICENSE = "LICENSE"

setup_args = dict(
    name                 = NAME,
    version              = VERSION,
    description          = DESCR,
    long_description     = open('README.rst').read(),
    author               = AUTHOR,
    author_email         = EMAIL,
    license              = LICENSE,
    keywords             = KEYWORDS,
    url                  = URL,
)

# ...
packages = find_packages(exclude=[])
# ...

def setup_package():
    setup(packages=packages, \
          zip_safe=False, \
          include_package_data=True, \
          **setup_args)

if __name__ == "__main__":
    setup_package()
