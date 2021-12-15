from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_anuales_demo_final.xlsx',
    'series': {
        'profesionales_medicina': {
            'sheet': 'Profesionales sanitarios',
            'label': 'Médicas/os no jubilados por 100.000 hab',
            'category': 'Profesionales sanitarios colegiados',
            'variables': [
                'Médicas/os no jubilados por 100.000 hab_Cantabria',
                'Médicas/os no jubilados por 100.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Profesionales Sanitarios Colegiados, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'profesionales-medicina.json-stat'
        },
        'profesionales_enfermeria': {
            'sheet': 'Profesionales sanitarios',
            'label': 'Enfermeras/os no jubilados 100.000 hab',
            'category': 'Profesionales sanitarios colegiados',
            'variables': [
                'Enfermeras/os no jubilados 100.000 hab_Cantabria',
                'Enfermeras/os no jubilados 100.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Profesionales Sanitarios Colegiados, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'profesionales-enfermeria.json-stat'
        },
    },
    'globals': {
        'csv': 'vision-global-salud.csv'
    }
}

health_cfg = Baseconfig(params)
health_cfg.add(common_cfg)
