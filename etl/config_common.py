from beautifuldict.baseconfig import Baseconfig

from decouple import config

from pkg_resources import resource_filename

params = {
    'path': {
        'input': resource_filename(__name__, 'data/input/'),
        'output': resource_filename(__name__, 'data/output/')
    },
    'value_labels': {
        'month': {
            '1': 'Enero',
            '2': 'Febrero',
            '3': 'Marzo',
            '4': 'Abril',
            '5': 'Mayo',
            '6': 'Junio',
            '7': 'Julio',
            '8': 'Agosto',
            '9': 'Septiembre',
            '10': 'Octubre',
            '11': 'Noviembre',
            '12': 'Diciembre'
        }
    },
    'periods': {
        'global_demographics': 6,
        'demographics': 24,
	    'global_health': 6,
        'health': 24,
        'global_deaths': 6,
        'deaths': 24
    }
}

common_cfg = Baseconfig(params)
