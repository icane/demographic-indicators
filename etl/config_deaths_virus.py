from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_mensual_demo.xlsx',
    'series': {
        'tabla1': {
            'sheet': 'COVID de muerte meses',
            'label': 'Virus identificado',
            'category': 'COVID de muerte meses',
            'variables': [
                'COVID-19_Virus identificado_Cantabria',
                'COVID-19_Virus no identificado (sospechoso)_Cantabria',
                'Otras causas_Cantabria',
                'COVID-19_Virus identificado_España',
                'COVID-19_Virus no identificado (sospechoso)_España',
                'Otras causas_España',
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'COVID-19_Virus identificado_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_España': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_España': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'virus_identificado_tabla.json-stat'
        },
        'covid_identificado': {
            'sheet': 'COVID de muerte meses',
            'label': 'Virus identificado',
            'category': 'COVID de muerte meses',
            'variables': [
                'COVID-19_Virus identificado_Tanto x 1.000_Cantabria',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Cantabria',
                'Otras causas_Tanto x 1000_Cantabria',
                'COVID-19_Virus identificado_Tanto x 1.000.España',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_España',
                'Otras causas_Tanto x 1000_España',
                'COVID-19_Virus identificado_Tanto x 1.000_Mujeres Cantabria',
                'COVID-19_Virus identificado_Tanto x 1.000_Hombres Cantabria'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'COVID-19_Virus identificado_Tanto x 1.000_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_Tanto x 1000_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000.España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_España': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_Tanto x 1000_España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_Mujeres Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_Hombres Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid_identificado-1.json-stat'
        },
        'covid_identificado_cantabria': {
            'sheet': 'COVID de muerte meses',
            'label': 'Virus otras causas',
            'category': 'COVID de muerte meses',
            'variables': [
                'COVID-19_Virus identificado_Tanto x 1.000_Cantabria',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Cantabria',
                'Otras causas_Tanto x 1000_Cantabria',
                'COVID-19_Virus identificado_Tanto x 1.000.España',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_España',
                'Otras causas_Tanto x 1000_España',
                'COVID-19_Virus identificado_Tanto x 1.000_Mujeres Cantabria',
                'COVID-19_Virus identificado_Tanto x 1.000_Hombres Cantabria'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'COVID-19_Virus identificado_Tanto x 1.000_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_Tanto x 1000_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000.España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_España': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_Tanto x 1000_España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_Mujeres Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_Hombres Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-identificado-cantabria.json-stat'
        },
        'covid_identificado_sexo': {
            'sheet': 'COVID de muerte meses',
            'label': 'Virus otras causas',
            'category': 'COVID de muerte meses',
            'variables': [
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Mujeres Cantabria',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Hombres Cantabria',
                'Otras causas_Tanto x 1000_Mujeres Cantabria',
                'Otras causas_Tanto x 1000_Hombres Cantabria',
                'COVID-19_Virus identificado_Tanto x 1.000_Mujeres España',
                'COVID-19_Virus identificado_Tanto x 1.000_Hombres España',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Mujeres España',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Hombres España',
                'Otras causas_Tanto x 1000_Mujeres España',
                'Otras causas_Tanto x 1000_Hombres España'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Mujeres Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Hombres Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_Tanto x 1000_Mujeres Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_Tanto x 1000_Hombres Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_Mujeres España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_Hombres España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Mujeres España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Hombres España': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_Tanto x 1000_Mujeres España': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas_Tanto x 1000_Hombres España': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-identificado-sexo.json-stat'
        },
        'covid_tasas': {
            'sheet': 'COVID de muerte meses',
            'label': 'Virus otras causas',
            'category': 'COVID de muerte meses',
            'variables': [
                'COVID-19_Virus identificado_Tanto x 1.000_Hasta 64  años_Cantabria',
                'COVID-19_Virus identificado_Tanto x 1.000_65-74 años_Cantabria',
                'COVID-19_Virus identificado_Tanto x 1.000_De 75 a 79 años_Cantabria',
                'COVID-19_Virus identificado_Tanto x 1.000_De 80 a 84 años_Cantabria',
                'COVID-19_Virus identificado_Tanto x 1.000_De 85 y +_Cantabria'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'COVID-19_Virus identificado_Tanto x 1.000_Hasta 64  años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_65-74 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_De 75 a 79 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_De 80 a 84 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_De 85 y +_Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-identificado-tasas.json-stat'
        },
        'covid_tasas_edad': {
            'sheet': 'COVID de muerte meses',
            'label': 'Virus otras causas',
            'category': 'COVID de muerte meses',
            'variables': [
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Hasta 64  años_Cantabria',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_65-74 años_Cantabria',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_De 75 a 79 años_Cantabria',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_De 80 a 84 años_Cantabria',
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_De 85 y +_Cantabria'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_Hasta 64  años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_65-74 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_De 75 a 79 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_De 80 a 84 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus no identificado (sospechoso)_Tanto x 1.000_De 85 y +_Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-tasas-edad.json-stat'
        },
        'covid_identificado_otras': {
            'sheet': 'COVID de muerte meses',
            'label': 'Virus otras causas',
            'category': 'COVID de muerte meses',
            'variables': [
                'COVID-19_Virus identificado_Tanto x 1.000_Hasta 64  años_España',
                'COVID-19_Virus identificado_Tanto x 1.000_65-74 años_España',
                'COVID-19_Virus identificado_Tanto x 1.000_De 75 a 79 años_España',
                'COVID-19_Virus identificado_Tanto x 1.000_De 80 a 84 años_España',
                'COVID-19_Virus identificado_Tanto x 1.000_De 85 y +_España'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'COVID-19_Virus identificado_Tanto x 1.000_Hasta 64  años_España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_65-74 años_España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_De 75 a 79 años_España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_De 80 a 84 años_España': {'decimals': 0, 'label': 'Defunciones'},
                'COVID-19_Virus identificado_Tanto x 1.000_De 85 y +_España': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-otras.json-stat'
        }
    },
    'globals': {
        'csv': 'vision-global-defunciones-virus.csv'
    }
}

deaths_cfg = Baseconfig(params)
deaths_cfg.add(common_cfg)
