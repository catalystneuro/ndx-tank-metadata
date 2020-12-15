# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Get the long description from the README file
with open('README.md', 'r') as f:
    long_description = f.read()

# Get requirements
with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='ndx-tank-metadata',
    version='0.1.0',
    description='NWB:N extension for storing metadata for Tank lab',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Szonja Weigl, Luiz Tauffer and Ben Dichter',
    email='ben.dichter@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.yml', '*.json']},
    install_requires=install_requires,
)