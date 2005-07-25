try:
    # if you want to build python egg dist files,
    # you'll need the latest version of setuptools
    # You can get it in the nondist/sandbox/setuptools
    # directory in a python cvs checkout.
    from setuptools import setup
except:
    from distutils.core import setup

setup(name="PyMonitor",
    version=open('VERSION').read(),
    description="A curses MMPORG game based on the Rook Saga universe",
    author="Duncan McGreggor",
    author_email="duncan@adytum.us",
    url="http://projects.adytum.us/tracs/RookSaga/wiki/CursesTheRookses",
    license="BSD",
    long_description='',
    packages=[
        'adytum',
        'adytum.games',
        'adytum.games.rookcurses',
        'adytum.urwid',
        'adytum.imagination',
        'adytum.imagination.templates',
        'adytum.imagination.test',
        'adytum.imagination.text',
        'adytum.imagination.wiring',
    ],
    package_dir = {'adytum': 'lib'},
)

