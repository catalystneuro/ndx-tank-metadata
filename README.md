# ndx-tank-metadata

NWB LabMetaData extension for [Tank lab](https://pni.princeton.edu/faculty/david-tank).

# Install

```
$ pip install ndx-tank-metadata
```

# Usage

This extension is built for extending the LabMetaData schema with custom fields requested for the
conversion of Virmen metadata. The extension is built into the Tank lab conversion
pipeline ([tank-lab-to-nwb](https://github.com/catalystneuro/tank-lab-to-nwb)) and is not necessary
to be installed separately. Alternatively, it can be used from a python script as demonstrated below.

```python
import os
from pynwb import NWBFile, NWBHDF5IO
from datetime import datetime

from ndx_tank_metadata import LabMetaDataExtension, RigExtension, MazeExtension

nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

# Add rig information
rig = {'name': 'rig',
       'rig': 'VRTrain6',
       'simulationMode': 0,
       'hasDAQ': 1,
       'hasSyncComm': 0,
       'minIterationDT': 0.01,
       'arduinoPort': 'COM5',
       'sensorDotsPerRev': [1967.6, 1967.6, 1967.6, 1967.6],
       'ballCircumference': 63.8,
       'toroidXFormP1': 0.5193,
       'toroidXFormP2': 0.5171,
       'colorAdjustment': [0., 0.4, 0.5],
       'soundAdjustment': 0.2,
       'nidaqDevice': 1,
       'nidaqPort': 1,
       'nidaqLines': [0, 11],
       'syncClockChannel': 5,
       'syncDataChannel': 6,
       'rewardChannel': 0,
       'rewardSize': 0.004,
       'rewardDuration': 0.05,
       'laserChannel': 1,
       'rightPuffChannel': 2,
       'leftPuffChannel': 3,
       'webcam_name': 'Live! Cam Sync HD VF0770'}
rig_extension = RigExtension(**rig)

# Create mazes table
maze_extension = MazeExtension(name='mazes',
                               description='description of the mazes')

maze_dict = {'world': 1,
             'lStart': '5',
             'lCue': '45',
             'lMemory': '10',
             'cueDuration': 'NaN',
             'cueVisibleAt': 'Inf',
             'cueProbability': 'Inf',
             'cueDensityPerM': '3',
             'nCueSlots': '3',
             'tri_turnHint': 1,
             'color': [],
             'turnHint_Mem': 0,
             'numTrials': 10,
             'numTrialsPerMin': 2,
             'criteriaNTrials': 1,
             'warmupNTrials': [],
             'numSessions': 0,
             'performance': 0, 
             'maxBias': 1,
             'warmupMaze': [],
             'warmupPerform': [],
             'warmupBias': [],
             'warmupMotor': [],
             'easyBlock': 0,
             'easyBlockNTrials': 10,
             'numBlockTrials': 20,
             'blockPerform': 0.7}

# Add each maze to extension
maze_extension.add_row(**maze_dict)

# Create LabMetaData container
lab_metadata_dict = dict(
    name='LabMetaData',
    experiment_name='test',
    world_file_name='test',
    protocol_name='test',
    stimulus_bank_path='test',
    commit_id='test',
    location='test',
    num_trials=245,
    session_end_time=datetime.utcnow().isoformat(),
    rig=rig_extension,
    mazes=maze_extension
)

# Populate metadata extension 
lab_metadata = LabMetaDataExtension(**lab_metadata_dict)

# Add to file
nwbfile.add_lab_meta_data(lab_metadata)

filename = 'test_labmetadata.nwb'
with NWBHDF5IO(filename, 'w') as io:
    io.write(nwbfile)

```