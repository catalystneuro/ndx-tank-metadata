import os
from pynwb import NWBFile, NWBHDF5IO
import unittest
from datetime import datetime

from src.pynwb.ndx_tank_metadata import LabMetaDataExtension


class LabMetaDataExtensionTest(unittest.TestCase):

    def setUp(self):
        self.nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    def test_add_lab_metadata(self):
        # Creates LabMetaData container

        lab_metadata_dict = dict(
            name='LabMetaData',
            experiment_name='test',
            world_file_name='test',
            protocol_name='test',
            stimulus_bank_path='test',
            commit_id='test',
            location='test',
            session_performance=1.,
        )

        lab_metadata = LabMetaDataExtension(**lab_metadata_dict)

        # Add to file
        self.nwbfile.add_lab_meta_data(lab_metadata)

        filename = 'test_labmetadata.nwb'

        with NWBHDF5IO(filename, 'w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(filename, mode='r', load_namespaces=True) as io:
            nwbfile = io.read()

            for k, v in lab_metadata_dict.items():
                self.assertEqual(v, getattr(nwbfile.lab_meta_data['LabMetaData'], k, None))

        os.remove(filename)
