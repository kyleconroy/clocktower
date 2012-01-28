#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='clocktower',
    version='0.1.0',
    author='Kyle Conroy',
    author_email='kyle@twilio.com',
    url='https://github.com/derferman/clocktower',
    description='Download websites from Wayback Machine',
    install_requires=['lxml'],
    data_files=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    entry_points={
        'console_scripts': [
            'clocktower = clocktower:main']
    },
)
