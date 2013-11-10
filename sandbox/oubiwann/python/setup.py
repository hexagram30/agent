from setuptools import setup, find_packages


setup(i
    name="innoþ",
    version="0.1",
    description="Python libraries for behavioral and emotional modeling",
    author="Duncan McGreggor",
    author_email="duncan@adytum.us",
    url="git@github.com:oubiwann/innoth.git",
    install_requires=[
        "numpy",
        "zope.interface",
        ],
    packages=find_packages(),
)
