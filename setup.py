#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup for urlextract

.. Created on 2016-07-29
.. Licence MIT
.. codeauthor:: Jan Lipovský <janlipovsky@gmail.com>, janlipovsky.cz
"""

import os
from distutils.core import setup

script_dirname = os.path.join(os.path.dirname(__file__))

__VERSION__ = None
# get __VERSION__ variable from file
version_file = os.path.join(script_dirname, 'version.py')
exec(open(version_file).read())


def read(readme):
    return open(os.path.join(script_dirname, readme)).read()

setup(
    name='urlextract-py2.7',
    version=__VERSION__,
    py_modules=['urlextract', 'version'],
    keywords=['url', 'extract', 'find', 'finder', 'collect', 'link', 'tld', 'list'],
    url='https://github.com/penafieljlm/URLExtract-py2.7',
    license='MIT',
    author='John Lawrence M. Penafiel',
    author_email='penafieljlm@gmail.com',
    description='Collects and extracts URLs from given text. Forked from https://pypi.python.org/pypi/urlextract.',
    long_description='Collects and extracts URLs from given text. Forked from https://pypi.python.org/pypi/urlextract.',
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python",
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Text Processing',
                 "Topic :: Text Processing :: Markup :: HTML",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 ],
    install_requires=[
        'idna',
        'uritools'
    ],
)
