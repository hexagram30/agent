#!/usr/bin/env python

from distutils.core import setup

setup(name="PyRookSaga",
    version="1.0",
    description="RookSaga Python Libraries",
    author="Duncan McGreggor",
    author_email="duncan@adytumsolutions.com",
    url="http://rooksaga.net",
    packages=[
        'adytum',
        'adytum/behavior',
        'adytum/environment',
        'adytum/graphics',
        'adytum/math',
        'adytum/personality',
        'adytum/personality/astrology',
        'adytum/personality/biorhythms',
    ],
)
