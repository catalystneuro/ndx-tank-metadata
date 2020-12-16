import os
from pynwb import NWBFile, NWBHDF5IO
import unittest
from datetime import datetime

from src.pynwb.ndx_tank_metadata import LabMetaDataExtension


class LabMetaDataExtensionTest(unittest.TestCase):

    def setUp(self):
        self.nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    def test_add_lab_metadata(self):
        metadata_fields = dict(experiment_name='test',
                               world_file_name='test',
                               protocol_name='test',
                               stimulus_bank_path='test',
                               commit_id='test',
                               location='test',
                               session_performance=1.,)

        # Creates LabMetaData container
        lab_metadata = LabMetaDataExtension(name='LabMetaData',
                                            **metadata_fields)

        # Add to file
        self.nwbfile.add_lab_meta_data(lab_metadata)

        filename = 'test_labmetadata.nwb'

        with NWBHDF5IO(filename, 'w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(filename, mode='r', load_namespaces=True) as io:
            nwb = io.read()

        assert nwb.lab_meta_data['LabMetaData'].fields == metadata_fields

        os.remove(filename)
