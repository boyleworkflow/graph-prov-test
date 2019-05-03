#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author='Rasmus Einarsson and Jonatan Kallus',
    author_email=(
        'mr [at] rasmuseinarsson [dot] se, mr [at] jkallus [dot] se'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A tool for provenance and caching in computational workflows.",
    entry_points={
        'console_scripts': [
            'boyle=boyle.cli:main',
        ],
    },
    install_requires=requirements,
    license="LGPLv3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='boyle',
    name='boyle',
    packages=find_packages(include=['boyle']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/boyleworkflow/boyle',
    version='0.1.0',
    zip_safe=False,
)
