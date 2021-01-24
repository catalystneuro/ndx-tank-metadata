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
        required=False
    )

    LabMetaDataExtension.add_attribute(
        name='session_end_time',
        doc='Datetime when session ended',
        dtype='text',  # temporary solution until datetime is fixed
    )

    LabMetaDataExtension.add_attribute(
        name='num_trials',
        doc='Number of trials during the session',
        dtype='int',
    )

    RigExtension = NWBGroupSpec(
        doc='type for storing rig information',
        neurodata_type_def='RigExtension',
        neurodata_type_inc='LabMetaData',
    )

    rig_attr = [('rig', 'text'), ('simulationMode', 'int'), ('hasDAQ', 'int'),
                ('hasSyncComm', 'int'), ('minIterationDT', 'float'), ('arduinoPort', 'text'),
                ('sensorDotsPerRev', 'float'), ('ballCircumference', 'float'),
                ('toroidXFormP1', 'float'), ('toroidXFormP2', 'float'),
                ('colorAdjustment', 'float'), ('soundAdjustment', 'float'),
                ('nidaqDevice', 'int'), ('nidaqPort', 'int'), ('nidaqLines', 'int'),
                ('syncClockChannel', 'int'), ('syncDataChannel', 'int'),
                ('rewardChannel', 'int'), ('rewardSize', 'float'),
                ('rewardDuration', 'float'), ('laserChannel', 'int'),
                ('rightPuffChannel', 'int'), ('leftPuffChannel', 'int'), ('webcam_name', 'text')]
    for attr in rig_attr:
        if attr[0] in ['sensorDotsPerRev', 'colorAdjustment', 'nidaqLines']:
            RigExtension.add_attribute(
                name=attr[0],
                doc='rig information',
                dtype=attr[1],
                shape=(None,),
                required=False
            )
        else:
            RigExtension.add_attribute(
                name=attr[0],
                doc='rig information',
                dtype=attr[1],
                required=False
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
