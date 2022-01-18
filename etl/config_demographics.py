from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_anuales_demo.xlsx',
    'series': {
    },
    'globals': {
        'csv': 'vision-global-demografia.csv'
    }
}

demographics_cfg = Baseconfig(params)
demographics_cfg.add(common_cfg)
