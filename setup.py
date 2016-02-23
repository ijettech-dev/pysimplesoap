#!/usr/bin/env python

from setuptools import setup
from pysimplesoap import __version__, __author__, __author_email__, __license__

build_installer = None

# convert the README and format in restructured text (only when registering)
long_desc = ""

setup(
    name='PySimpleSOAP',
    version=__version__,
    description='Python simple and lightweight SOAP Library',
    long_description=long_desc,
    author=__author__,
    author_email=__author_email__,
    url='http://code.google.com/p/pysimplesoap',
    packages=['pysimplesoap'],
    license=__license__,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
