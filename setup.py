#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="hangman",
    version="0.0.0",
    author="care1e55",
    author_email="sfilms89@gmail.com",
    url="https://github.com/care1e55/hangman",
    license="MIT",
    packages=[
        # "hangman",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
