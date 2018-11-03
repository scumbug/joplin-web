#!/usr/bin/env python
# coding: utf-8
import os
from setuptools import setup, find_packages
from joplin_web import __version__ as version


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))


install_requires = reqs('requirements.txt')


setup(
    name='joplin_web',
    version=version,
    description='Joplin Web',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # This is important!
    author='FoxMaSk',
    maintainer='FoxMaSk',
    author_email='foxmask protonmail',
    maintainer_email='foxmask protonmail',
    url='https://github.com/foxmask/joplin-web',
    download_url="https://github.com/foxmask/joplin-web/archive/joplin_web-" + version + ".zip",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Database',
    ],
    install_requires=install_requires,
    include_package_data=True,
)
