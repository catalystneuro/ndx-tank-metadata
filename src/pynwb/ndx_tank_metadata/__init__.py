import os
from pynwb import load_namespaces, get_class

name = 'ndx-tank-metadata'

spec_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
ns_path = os.path.join(spec_path, 'spec', f'{name}.namespace.yaml')

load_namespaces(ns_path)

LabMetaDataExtension = get_class('LabMetaDataExtension', name)
