import os
from pynwb import load_namespaces, register_class
from pynwb.file import DynamicTable
from hdmf.utils import docval, call_docval_func, get_docval

name = 'ndx-tank-metadata'

spec_path = os.path.abspath(os.path.dirname(__file__))
ns_path = os.path.join(spec_path, 'spec', f'{name}.namespace.yaml')

load_namespaces(ns_path)

@register_class('MazeExtension', name)
class MazeExtension(DynamicTable):
    """
    Table for storing maze information
    """

    mazes_attr = ['world', 'lStart', 'lCue', 'lMemory', 'cueDuration', 'cueVisibleAt',
                  'cueProbability', 'cueDensityPerM', 'antiFraction', 'nCueSlots', 'tri_turnHint',
                  'color', 'numTrials', 'numTrialsPerMin', 'criteriaNTrials', 'warmupNTrials',
                  'numSessions', 'performance', 'maxBias', 'warmupMaze', 'warmupPerform',
                  'warmupBias', 'warmupMotor', 'easyBlock', 'easyBlockNTrials', 'numBlockTrials',
                  'blockPerform']

    __columns__ = tuple(
        {'name': attr, 'description': 'maze information', 'required': False, 'index': False,
         'table': False} for attr in mazes_attr
    )

    @docval(dict(name='name', type=str, doc='name of this MazeExtension'),  # required
            dict(name='description', type=str, doc='Description of this DynamicTable'),
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        call_docval_func(super(MazeExtension, self).__init__, kwargs)
