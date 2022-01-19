from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_mensual_demo.xlsx',
    'series': {
        'mortalidad': {
            'sheet': 'COVID de muerte meses',
            'label': 'COVID-19 Virus identificado',
            'category': 'Tasas de mortalidad',
            'variables': [
                'COVID-19_Virus identificado_Cantabria',
                'COVID-19_Virus no identificado (sospechoso)_Cantabria',
                'Otras causas_Cantabria',
                'COVID-19_Virus identificado_España',
                'COVID-19_Virus no identificado (sospechoso)_España',
                'Otras causas_España'],
            'source': 'ICANE a partir de la explotación de Estadística de defunciones según la causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 0, 'label': 'Tanto por cienmil'},
                'Cantabria_MM': {'decimals': 0, 'label': 'Tanto por cienmil'},
                'España_MM': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': 'virus-identificado.json-stat'
        }
    },
    'globals': {
        'csv': 'vision-global-defunciones-virus.csv'
    }
}

deaths_cfg = Baseconfig(params)
deaths_cfg.add(common_cfg)
