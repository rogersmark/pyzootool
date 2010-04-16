import os
from setuptools import setup, find_packages

setup(
    name = "pyzootool",
    version = "0.2",
    author = "Mark Rogers",
    author_email = "f4nt@f4ntasmic.com",
    url = "http://www.f4ntasmic.com",

    packages = find_packages('.'),
    package_dir = {'':'.'},
    data_files=[('.', ['README',]),],
    package_data = {
    },
    include_package_data=True,

    keywords = "zootool socialmedia api",
    description = "A wrapper of the zootool.com API",
    install_requires=[
        "httplib2",
    ],
    classifiers = [
        "Intended Audience :: Developers",
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
    ]
)
