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
        'adytum/aima',
        'adytum/behavior',
        'adytum/emotion',
        'adytum/environment',
        'adytum/graphics',
        'adytum/math',
        'adytum/perception',
        'adytum/personality',
        'adytum/personality/astrology',
        'adytum/personality/biorhythms',
        'adytum/physiology',
    ],
)
