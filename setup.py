"""A setuptools based setup module for BloomSky-API"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'requests',
]

test_requirements = [
]

setup(
    name='BloomSky-API',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A simple Python client for the BloomSky API.",
    long_description=readme + '\n\n' + history,
    author="Dave Forgac",
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/bloomsky-api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts':[
            'bloomsky-api=bloomsky_api.cli:cli',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
        'cli': ["click>=5"],
        }
)
