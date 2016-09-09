import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mast.cron",
    version = "2.2.0",
    author = "Clifford Bressette",
    author_email = "cliffordbressette@mcindi.com",
    description = ("A cron-style scheduler"),
    license = "GPLv3",
    keywords = "cron daemon scheduler",
    url = "http://github.com/mcindi/mast.cron",
    namespace_packages=["mast"],
    packages=['mast', 'mast.cron'],
    entry_points = {
        'mastd_plugin': [
            'mastd_cron_plugin = mast.cron:Plugin'
        ]
    },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv3",
    ],
    install_requires=["mast.logging", "mast.config", "mast.daemon"]
)

