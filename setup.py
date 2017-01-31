# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Test project for RMR',
    'author': 'Kseniya Tychkova',
    'author_email': 'kseniya.tychkova@gmail.com',
    'version': '0.1',
    'packages': ['rmrvector'],
    'scripts': [],
    'name': 'rmrvector'
}

setup(**config)
