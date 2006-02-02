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
        'adytum/action',
        'adytum/agent',
        'adytum/aima',
        'adytum/archetypes',
        'adytum/behavior',
        'adytum/body',
        'adytum/decision',
        'adytum/emotion',
        'adytum/environment',
        'adytum/event',
        'adytum/graphics',
        'adytum/graphics/agraph',
        'adytum/math',
        'adytum/mind',
        'adytum/personality',
        'adytum/personality/astrology',
        'adytum/personality/biorhythms',
        'adytum/planner',
        'adytum/relationship',
        'adytum/world',
    ],
)
