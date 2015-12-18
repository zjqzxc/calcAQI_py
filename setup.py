import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "AQI"
PACKAGES = ["AQI",]
DESCRIPTION = "Calculate the AQI(Air Quality Index) by the pollution concentration"
LONG_DESCRIPTION = read("README.rst")
KEYWORDS = "AQI aqi"
AUTHOR = "Flagplus"
AUTHOR_EMAIL = "i@flagplus.net"
URL = "https://github.com/zjqzxc/calcAQI_py"
VERSION = "0.1"
LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)