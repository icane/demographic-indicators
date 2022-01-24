from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_mensual_demo.xlsx',
    'series': {
        'tabla1': {
            'sheet': 'COVID de muerte meses',
            'label': 'Defunciones por COVID-19',
            'category': 'Defunciones por COVID-19',
            'variables': [
                'Virus identificado Cantabria',
                'Virus no identificado (sospechoso) Cantabria',
                'Otras causas Cantabria',
                'Virus identificado España',
                'Virus no identificado (sospechoso) España',
                'Otras causas España',
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Virus identificado Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) España': {'decimals': 0, 'label': 'Defunciones'},
                'Otras causas España': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'virus_identificado_tabla.json-stat'
        },
        'covid_identificado': {
            'sheet': 'COVID de muerte meses',
            'label': 'Tasas de mortalidad COVID-19',
            'category': 'Tasas de mortalidad COVID-19',
            'variables': [
                'Virus identificado Tanto x 1.000 Cantabria',
                'Virus no identificado (sospechoso) Tanto x 1.000 Cantabria',
                'Virus identificado Tanto x 1.000.España',
                'Virus no identificado (sospechoso) Tanto x 1.000 España',
                'Virus identificado Tanto x 1.000 Mujeres Cantabria',
                'Virus identificado Tanto x 1.000 Hombres Cantabria'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Virus identificado Tanto x 1.000 Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000.España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 Mujeres Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 Hombres Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid_identificado-1.json-stat'
        },
        'covid_identificado_sexo': {
            'sheet': 'COVID de muerte meses',
            'label': 'Tasas de mortalidad COVID-19 por sexo',
            'category': 'Tasas de mortalidad COVID-19 por sexo',
            'variables': [
                'Virus no identificado (sospechoso) Tanto x 1.000 Mujeres Cantabria',
                'Virus no identificado (sospechoso) Tanto x 1.000 Hombres Cantabria',
                'Virus identificado Tanto x 1.000 Mujeres España',
                'Virus identificado Tanto x 1.000 Hombres España',
                'Virus no identificado (sospechoso) Tanto x 1.000 Mujeres España',
                'Virus no identificado (sospechoso) Tanto x 1.000 Hombres España'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Virus no identificado (sospechoso) Tanto x 1.000 Mujeres Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 Hombres Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 Mujeres España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 Hombres España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 Mujeres España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 Hombres España': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-identificado-sexo.json-stat'
        },
        'covid_tasas': {
            'sheet': 'COVID de muerte meses',
            'label': 'Tasas de mortalidad COVID-19 virus identificado por grupos de edad. Cantabria',
            'category': 'Tasas de mortalidad COVID-19 virus identificado por grupos de edad. Cantabria',
            'variables': [
                'Virus identificado Tanto x 1.000 Hasta 64 años Cantabria',
                'Virus identificado Tanto x 1.000 65-74 años Cantabria',
                'Virus identificado Tanto x 1.000 De 75 a 79 años Cantabria',
                'Virus identificado Tanto x 1.000 De 80 a 84 años Cantabria',
                'Virus identificado Tanto x 1.000 De 85 y + Cantabria'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Virus identificado Tanto x 1.000 Hasta 64 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 65-74 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 De 75 a 79 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 De 80 a 84 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 De 85 y + Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-identificado-tasas.json-stat'
        },
        'covid_tasas_edad': {
            'sheet': 'COVID de muerte meses',
            'label': 'Tasas de mortalidad COVID-19 sospechoso por grupos de edad. Cantabria',
            'category': 'Tasas de mortalidad COVID-19 sospechoso por grupos de edad. Cantabria',
            'variables': [
                'Virus no identificado (sospechoso) Tanto x 1.000 Hasta 64 años Cantabria',
                'Virus no identificado (sospechoso) Tanto x 1.000 65-74 años Cantabria',
                'Virus no identificado (sospechoso) Tanto x 1.000 De 75 a 79 años Cantabria',
                'Virus no identificado (sospechoso) Tanto x 1.000 De 80 a 84 años Cantabria',
                'Virus no identificado (sospechoso) Tanto x 1.000 De 85 y + Cantabria'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Virus no identificado (sospechoso) Tanto x 1.000 Hasta 64 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 65-74 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 De 75 a 79 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 De 80 a 84 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 De 85 y + Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-tasas-edad.json-stat'
        },
        'covid_identificado_otras': {
            'sheet': 'COVID de muerte meses',
            'label': 'Tasas de mortalidad COVID-19 virus identificado por grupos de edad. España',
            'category': 'Tasas de mortalidad COVID-19 virus identificado por grupos de edad. España',
            'variables': [
                'Virus identificado Tanto x 1.000 Hasta 64 años España',
                'Virus identificado Tanto x 1.000 65-74 años España',
                'Virus identificado Tanto x 1.000 De 75 a 79 años España',
                'Virus identificado Tanto x 1.000 De 80 a 84 años España',
                'Virus identificado Tanto x 1.000 De 85 y + España'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Virus identificado Tanto x 1.000 Hasta 64 años España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 65-74 años España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 De 75 a 79 años España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 De 80 a 84 años España': {'decimals': 0, 'label': 'Defunciones'},
                'Virus identificado Tanto x 1.000 De 85 y + España': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-otras.json-stat'
        },
        'covid_tasas_edad_espana': {
            'sheet': 'COVID de muerte meses',
            'label': 'Tasas de mortalidad COVID-19 sospechoso por grupos de edad. España',
            'category': 'Tasas de mortalidad COVID-19 sospechoso por grupos de edad. España',
            'variables': [
                'Virus no identificado (sospechoso) Tanto x 1.000 Hasta 64 años España',
                'Virus no identificado (sospechoso) Tanto x 1.000 65-74 años España',
                'Virus no identificado (sospechoso) Tanto x 1.000 De 75 a 79 años España',
                'Virus no identificado (sospechoso) Tanto x 1.000 De 80 a 84 años España',
                'Virus no identificado (sospechoso) Tanto x 1.000 De 85 y + España'
            ],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Virus no identificado (sospechoso) Tanto x 1.000 Hasta 64 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 65-74 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 De 75 a 79 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 De 80 a 84 años Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Virus no identificado (sospechoso) Tanto x 1.000 De 85 y + Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'covid-tasas-edad_espana.json-stat'
        },
    },
    'globals': {
        'csv': 'vision-global-defunciones-virus.csv'
    }
}

deaths_cfg = Baseconfig(params)
deaths_cfg.add(common_cfg)
