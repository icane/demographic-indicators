from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_anuales_demo_final.xlsx',
    'series': {
        'padron_interanual': {
            'sheet': 'Demografía',
            'label': 'Variación interanual de empadronados',
            'category': 'Población empadronada 1 de enero',
            'variables': [
                'Variación interanual empadronas_Cantabria',
                'Variación interanual empadronas_España'],
            'source': 'ICANE a partir de la explotación de microdatos del Padrón Municipal de Habitantes, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': '%'},
                'España': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'padron-interanual.json-stat'
        },
        'tasa_feminidad': {
            'sheet': 'Demografía',
            'label': 'Tasa de feminidad',
            'category': 'Población empadronada 1 de enero',
            'variables': [
                'Tasa de feminidad_Cantabria',
                'Tasa de feminidad_España'],
            'source': 'ICANE a partir de la explotación de microdatos del Padrón Municipal de Habitantes, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': '%'},
                'España': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'tasa-feminidad.json-stat'
        },
        'poblacion60': {
            'sheet': 'Demografía',
            'label': 'Proporción de población de 60 y más años',
            'category': 'Población empadronada 1 de enero',
            'variables': [
                'Propoción de 60 y más años_Canatbria',
                'Propoción de 60 y más años_España'],
            'source': 'ICANE a partir de la explotación de microdatos del Padrón Municipal de Habitantes, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': '%'},
                'España': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'poblacion60.json-stat'
        },
        'tasa_feminidad60': {
            'sheet': 'Demografía',
            'label': 'Tasa de feminidad 60 y más años',
            'category': 'Población empadronada 1 de enero',
            'variables': [
                'Tasa de feminidad 60 y más años_Cantabria',
                'Tasa de feminidad 60 y más años_España'],
            'source': 'ICANE a partir de la explotación de microdatos del Padrón Municipal de Habitantes, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': '%'},
                'España': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'tasa-feminidad60.json-stat'
        },
        'hogares_unipersonales': {
            'sheet': 'Demografía',
            'label': 'Proporción de hogares unipersonales',
            'category': 'Hogares',
            'variables': [
                'Porporción de hogares unipersonales_Cantabria',
                'Porporción de hogares unipersonales_España'],
            'source': 'ICANE a partir de la Encuesta Continua de Hogares, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': '%'},
                'España': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'hogares-unipersonales.json-stat'
        },
        'hogares_unipersonales65': {
            'sheet': 'Demografía',
            'label': 'Proporción de hogares unipersonales de 65 y más años',
            'category': 'Hogares',
            'variables': [
                'Proporción de hogares unipersonales de 65 y más años_Cantabria',
                'Proporción de hogares unipersonales de 65 y más años_España'],
            'source': 'ICANE a partir de la Encuesta Continua de Hogares, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': '%'},
                'España': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'hogares-unipersonales65.json-stat'
        },
        'feminidad_hogares_unipersonales65': {
            'sheet': 'Demografía',
            'label': 'Tasas de feminidad hogares unipersonales de 65 y + años ',
            'category': 'Hogares',
            'variables': [
                'Tasas de feminidad hogares unipersonales de 65 y + años_Cantabria ',
                'Tasas de feminidad hogares unipersonales de 65 y + años_España '],
            'source': 'ICANE a partir de la Encuesta Continua de Hogares, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': '%'},
                'España': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'feminidad-hogares-unipersonales65.json-stat'
        },
    },
    'globals': {
        'csv': 'vision-global-demografia.csv'
    }
}

demographics_cfg = Baseconfig(params)
demographics_cfg.add(common_cfg)
