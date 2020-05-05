from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config

params = {
    'file': 'Mapas_muni.xlsx',
    'series': {
        'poblacion60': {
            'sheet': 'Mapas municipios',
            'label': 'Porcentaje de población de 60 y más años',
            'variables': ['COD_INE', '% pob 60y+'],
            'source': 'ICANE a partir de la explotación de microdatos del Padrón Municipal de Habitantes, INE',
            'unit':{
                'Porcentaje de población de 60 y más años': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'poblacion60-mapa.json-stat'
        },
        'poblacion60_hombres_hombres': {
            'sheet': 'Mapas municipios',
            'label': 'Porcentaje de hombres de 60 y más años respecto total hombres',
            'variables': ['COD_INE', '% H60_TH'],
            'source': 'ICANE a partir de la explotación de microdatos del Padrón Municipal de Habitantes, INE',
            'unit':{
                'Porcentaje de hombres de 60 y más años respecto total hombres': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'poblacion60-hombres-hombres-mapa.json-stat'
        },
        'poblacion60_hombres_poblacion': {
            'sheet': 'Mapas municipios',
            'label': 'Porcentaje de hombres de 60 y más años respecto al total de población',
            'variables': ['COD_INE', '% H60_TPOB'],
            'source': 'ICANE a partir de la explotación de microdatos del Padrón Municipal de Habitantes, INE',
            'unit':{
                'Porcentaje de hombres de 60 y más años respecto al total de población': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'poblacion60-hombres-poblacion-mapa.json-stat'
        },
        'poblacion60_mujeres_mujeres': {
            'sheet': 'Mapas municipios',
            'label': 'Porcentaje de mujeres de 60 y más años respecto total mujeres',
            'variables': ['COD_INE', '% M60_TM'],
            'source': 'ICANE a partir de la explotación de microdatos del Padrón Municipal de Habitantes, INE',
            'unit': {
                'Porcentaje de mujeres de 60 y más años respecto total mujeres': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'poblacion60-mujeres-mujeres-mapa.json-stat'
        },
        'poblacion60_mujeres_poblacion': {
            'sheet': 'Mapas municipios',
            'label': 'Porcentaje de mujeres de 60 y más años respecto al total de población',
            'variables': ['COD_INE', '% M60_TPOB'],
            'source': 'ICANE a partir de la explotación de microdatos del Padrón Municipal de Habitantes, INE',
            'unit':{
                'Porcentaje de mujeres de 60 y más años respecto al total de población': {'decimals': 2, 'label': '%'}
            },
            'note': [''],
            'json': 'poblacion60-mujeres-poblacion-mapa.json-stat'
        }
    }
}

maps_cfg = Baseconfig(params)
maps_cfg.add(common_cfg)
