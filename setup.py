#!/usr/bin/env python

import setuptools
import sys
import time
import pytest
import unittest

from pytest import ExitCode
from selenium import webdriver
from pages import *
from locators import *
from selenium.webdriver.common.by import By
from distutils.core import setup

class RegisterNewInstructor(unittest.TestCase):
      
setup(name='Distutils',
      version='3.x',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['distutils', 'distutils.command'],
     )

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-AnaGauna", # Replace with your own username
    version="0.0.1",
    author="Ana Gauna",
    author_email="amgauna@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amgauna/Python/.github/workflows/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

def pytest_load_initial_conftests(args):
    if "xdist" in sys.modules:  # pytest-xdist plugin
        import multiprocessing

        num = max(multiprocessing.cpu_count() / 2, 1)
        args[:] = ["-n", str(num)] + args
            
def test_placeholder():
    pass



