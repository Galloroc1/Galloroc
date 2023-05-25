from typing import Dict


default = {
    'role': 'guest',
    'ids': 0,
    'maps': {
        'guest': [0],
        'host': [1],
        'abiter': [], }
}


class Config:
    role = str
    maps = dict
    ids = int

    @classmethod
    def init(cls, maps=None):
        if maps is None:
            maps = default
        assert isinstance(maps, dict) and {'maps', 'role', 'ids'} == set(default.keys()), f'check your communicate maps'
        cls.maps = maps['maps']
        cls.role = maps['role']
        cls.ids = maps['ids']




