from setuptools import find_packages
from distutils.core import setup
from git_uploader import __version__

setup(
    name='git_uploader',
    version=__version__,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['git-uploader = git_uploader:main'],
    }
)
