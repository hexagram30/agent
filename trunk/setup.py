#!/usr/bin/env python

from distutils.core import setup

setup(name="EmotionalModeling",
    version="1.0",
    description="Python Libraries for Behavioral and Emotional Modeling",
    author="Duncan McGreggor",
    author_email="duncan@adytum.us",
    url="http://projects.adytum.us/tracs/EmotionalModeling",
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
