import os
from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec, export_spec


def main():
    ns_builder = NWBNamespaceBuilder(
        doc='type for storing metadata for Tank lab',
        name='ndx-tank-metadata',
        version='0.1.0',
        author=['Szonja Weigl', 'Luiz Tauffer', 'Ben Dichter'],
        contact=['ben.dichter@gmail.com']
    )

    ns_builder.include_type('LabMetaData', namespace='core')
    ns_builder.include_type('DynamicTable', namespace='core')

    LabMetaDataExtension = NWBGroupSpec(
        doc='type for storing metadata for Tank lab',
        neurodata_type_def='LabMetaDataExtension',
        neurodata_type_inc='LabMetaData',
    )

    LabMetaDataExtension.add_attribute(
        name='experiment_name',
        doc='name of experiment run',
        dtype='text',
    )

    LabMetaDataExtension.add_attribute(
        name='world_file_name',
        doc='name of world file run',
        dtype='text',
    )

    LabMetaDataExtension.add_attribute(
        name='protocol_name',
        doc='name of protocol run',
        dtype='text',
    )

    LabMetaDataExtension.add_attribute(
        name='stimulus_bank_path',
        doc='path of stimulus bank file',
        dtype='text',
    )

    LabMetaDataExtension.add_attribute(
        name='commit_id',
        doc='Commit id for session run',
        dtype='text',
    )

    LabMetaDataExtension.add_attribute(
        name='location',
        doc='Name of rig where session was run',
        dtype='text',
    )

    LabMetaDataExtension.add_attribute(
        name='session_performance',
        doc='Performance of correct responses in %',
        dtype='float',
    )

    RigExtension = NWBGroupSpec(
        doc='type for storing rig information',
        neurodata_type_def='RigExtension',
        neurodata_type_inc='LabMetaData',
    )

    rig_attr = ['rig', 'simulationMode', 'hasDAQ', 'hasSyncComm', 'minIterationDT', 'arduinoPort',
                'sensorDotsPerRev', 'ballCircumference', 'toroidXFormP1', 'toroidXFormP2',
                'colorAdjustment', 'soundAdjustment', 'nidaqDevice', 'nidaqPort', 'nidaqLines',
                'syncClockChannel', 'syncDataChannel', 'rewardChannel', 'rewardSize',
                'rewardDuration', 'laserChannel', 'rightPuffChannel', 'leftPuffChannel',
                'webcam_name']
    for attr in rig_attr:
        RigExtension.add_attribute(
            name=attr,
            doc='rig information',
            dtype='text',
        )

    LabMetaDataExtension.add_group(
        name='rig',
        neurodata_type_inc='RigExtension',
        doc='type for storing rig information',
    )

    MazeExtension = NWBGroupSpec(
        doc='type for storing maze information',
        neurodata_type_def='MazeExtension',
        neurodata_type_inc='DynamicTable',
    )

    LabMetaDataExtension.add_group(
        name='mazes',
        neurodata_type_inc='MazeExtension',
        doc='type for storing maze information',
    )

    # export the extension to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, [LabMetaDataExtension, RigExtension, MazeExtension], output_dir)


if __name__ == "__main__":
    main()
