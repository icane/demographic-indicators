from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config

params = {
    'file': 'Datos_carga_anuales_demo.xlsx',
    'tables': {
    },
    'globals': {
        'csv': 'vision-global-residencias.csv'
    }
}

residences_cfg = Baseconfig(params)
residences_cfg.add(common_cfg)
