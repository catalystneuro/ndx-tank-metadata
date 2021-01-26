# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from shutil import copy2
import os


# Get the long description from the README file
with open('README.md', 'r') as f:
    long_description = f.read()

# Get requirements
with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup_args = dict(
    name='ndx-tank-metadata',
    version='0.1.2',
    description='NWB:N extension for storing metadata for Tank lab',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Szonja Weigl, Luiz Tauffer and Ben Dichter',
    email='ben.dichter@gmail.com',
    url='https://github.com/catalystneuro/ndx-tank-metadata',
    packages=find_packages('src/pynwb'),
    package_dir={'': 'src/pynwb'},
    include_package_data=True,
    package_data={'ndx_tank_metadata': [
        'spec/ndx-tank-metadata.namespace.yaml',
        'spec/ndx-tank-metadata.extensions.yaml',
    ]},
    install_requires=install_requires,
)


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-tank-metadata.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-tank-metadata.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx_tank_metadata', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)
