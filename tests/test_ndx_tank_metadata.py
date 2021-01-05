import os
from pynwb import NWBFile, NWBHDF5IO
import unittest
from datetime import datetime

from src.pynwb.ndx_tank_metadata import LabMetaDataExtension, RigExtension, MazeExtension


class LabMetaDataExtensionTest(unittest.TestCase):

    def setUp(self):
        self.nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    def test_add_lab_metadata(self):
        # Add rig information
        rig = {'name': 'rig',
               'rig': 'VRTrain6',
               'simulationMode': '0',
               'hasDAQ': '1',
               'hasSyncComm': '0',
               'minIterationDT': '0.01',
               'arduinoPort': 'COM5',
               'sensorDotsPerRev': str([1967.6, 1967.6, 1967.6, 1967.6]),
               'ballCircumference': '63.8',
               'toroidXFormP1': '0.5193',
               'toroidXFormP2': '0.5171',
               'colorAdjustment': str([0., 0.4, 0.5]),
               'soundAdjustment': '0.2',
               'nidaqDevice': '1',
               'nidaqPort': '1',
               'nidaqLines': str([0, 11]),
               'syncClockChannel': '5',
               'syncDataChannel': '6',
               'rewardChannel': '0',
               'rewardSize': '0.004',
               'rewardDuration': '0.05',
               'laserChannel': '1',
               'rightPuffChannel': '2',
               'leftPuffChannel': '3',
               'webcam_name': 'Live! Cam Sync HD VF0770'}
        rig_extension = RigExtension(**rig)

        # Create mazes table
        maze_extension = MazeExtension(name='mazes',
                                       description='description of the mazes')
        mazes_dict = {k: ['test'] for k in maze_extension.colnames}
        maze_extension.add_row(**mazes_dict, id=0)

        # Creates LabMetaData container

        lab_metadata_dict = dict(
            name='LabMetaData',
            experiment_name='test',
            world_file_name='test',
            protocol_name='test',
            stimulus_bank_path='test',
            commit_id='test',
            location='test',
            rig=rig_extension,
            mazes=maze_extension
        )

        lab_metadata = LabMetaDataExtension(**lab_metadata_dict)

        # Add to file
        self.nwbfile.add_lab_meta_data(lab_metadata)

        filename = 'test_labmetadata.nwb'

        with NWBHDF5IO(filename, 'w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(filename, mode='r', load_namespaces=True) as io:
            nwbfile = io.read()

            for metadata_key, metadata_value in lab_metadata_dict.items():
                if isinstance(metadata_value, RigExtension):
                    for rig_key, rig_value in rig.items():
                        self.assertEqual(rig_value, getattr(metadata_value, rig_key, None))
                elif isinstance(metadata_value, MazeExtension):
                    for mazes_key, mazes_value in mazes_dict.items():
                        self.assertEqual(mazes_value, getattr(metadata_value, mazes_key, None).data)
                else:
                    self.assertEqual(metadata_value, getattr(nwbfile.lab_meta_data['LabMetaData'], metadata_key, None))

        os.remove(filename)
