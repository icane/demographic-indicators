from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_semanal_demo.xlsx',
    'series': {
        'mortalidad_total_base': {
            'sheet': '',
            'label': 'Dato base',
            'category': 'Mortalidad total',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-total-base.json-stat'
        },
        'mortalidad_total_acumulado': {
            'sheet': '',
            'label': 'Acumulado en lo que va de año',
            'category': 'Mortalidad total',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-total-acumulado.json-stat'
        },
        'mortalidad_total_variacion_acumulado': {
            'sheet': '',
            'label': 'Variación anual del acumulado en lo que va de año',
            'category': 'Mortalidad total',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-total-variacion-acumulado.json-stat'
        },
        'mortalidad_sexo_dato_base_hombres': {
            'sheet': '',
            'label': 'Dato base. Hombres',
            'category': 'Mortalidad por sexos',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-dato-base-hombres.json-stat'
        },
        'mortalidad_sexo_acumulado_hombres': {
            'sheet': '',
            'label': 'Acumulado en lo que va de año. Hombres',
            'category': 'Mortalidad por sexos',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-acumulado-hombres.json-stat'
        },
        'mortalidad_sexo_diferencia_acumulado_hombres': {
            'sheet': '',
            'label': 'Diferencia absoluta del acumulado. Hombres',
            'category': 'Mortalidad por sexos',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-diferencia-acumulado-hombres.json-stat'
        },
        'mortalidad_sexo_variacion_anual_acumulado_hombres': {
            'sheet': '',
            'label': 'Variación anual del acumulado en lo que va de año. Hombres',
            'category': 'Mortalidad por sexos',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-variacion-anual-acumulado-hombres.json-stat'
        },
        'mortalidad_sexo_dato_base_mujeres': {
            'sheet': '',
            'label': 'Dato base. Mujeres',
            'category': 'Mortalidad por sexos',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-dato-base-mujeres.json-stat'
        },
        'mortalidad_sexo_acumulado_mujeres': {
            'sheet': '',
            'label': 'Acumulado en lo que va de año. Mujeres',
            'category': 'Mortalidad por sexos',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-acumulado-mujeres.json-stat'
        },
        'mortalidad_sexo_diferencia_acumulado_mujeres': {
            'sheet': '',
            'label': 'Diferencia absoluta del acumulado. Mujeres',
            'category': 'Mortalidad por sexos',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-diferencia-acumulado-mujeres.json-stat'
        },
        'mortalidad_sexo_variacion_anual_acumulado_mujeres': {
            'sheet': '',
            'label': 'Variación anual del acumulado en lo que va de año. Mujeres',
            'category': 'Mortalidad por sexos',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-variacion-anual-acumulado-mujeres.json-stat'
        },
        'mortalidad_edades_base_hasta64': {
            'sheet': '',
            'label': 'Dato base. Hasta 64 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-hasta64.json-stat'
        },
        'mortalidad_edades_base_65_74': {
            'sheet': '',
            'label': 'Dato base. De 65 a 74 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-65-74.json-stat'
        },
        'mortalidad_edades_base_75_79': {
            'sheet': '',
            'label': 'Dato base. De 75 a 79 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-75-79.json-stat'
        },
        'mortalidad_edades_base_80_84': {
            'sheet': '',
            'label': 'Dato base. De 80 a 84 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-80-84.json-stat'
        },
        'mortalidad_edades_base_85_mas': {
            'sheet': '',
            'label': 'Dato base. De 85 y más años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-85-mas.json-stat'
        },
        'mortalidad_edades_acumulado_hasta64': {
            'sheet': '',
            'label': 'Acumulado en lo que va de año. Hasta 64 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-hasta64.json-stat'
        },
        'mortalidad_edades_acumulado_65_74': {
            'sheet': '',
            'label': 'Acumulado en lo que va de año. De 65 a 74 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-65-74.json-stat'
        },
        'mortalidad_edades_acumulado_75_79': {
            'sheet': '',
            'label': 'Acumulado en lo que va de año. De 75 a 79 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-75-79.json-stat'
        },
        'mortalidad_edades_acumulado_80_84': {
            'sheet': '',
            'label': 'Acumulado en lo que va de año. De 80 a 84 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-80-84.json-stat'
        },
        'mortalidad_edades_acumulado_85_mas': {
            'sheet': '',
            'label': 'Acumulado en lo que va de año. De 85 y más años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-85-mas.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado_hasta64': {
            'sheet': '',
            'label': 'Diferencia absoluta del acumulado. Hasta 64 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado-hasta64.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado_65_74': {
            'sheet': '',
            'label': 'Diferencia absoluta del acumulado. De 65 a 74 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado-65-74.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado_75_79': {
            'sheet': '',
            'label': 'Diferencia absoluta del acumulado. De 75 a 79 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado_75-79.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado-80_84': {
            'sheet': '',
            'label': 'Diferencia absoluta del acumulado. De 80 a 84 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado_80-84.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado-85_mas': {
            'sheet': '',
            'label': 'Diferencia absoluta del acumulado. De 85 y más años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado_85-mas.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_hasta64': {
            'sheet': '',
            'label': 'Variación anual del acumulado en lo que va de año. Hasta 64 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-hasta64.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_65_74': {
            'sheet': '',
            'label': 'Variación anual del acumulado en lo que va de año. De 65 a 74 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-65-74.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_75_79': {
            'sheet': '',
            'label': 'Variación anual del acumulado en lo que va de año. De 75 a 79 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-75-79.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_80_84': {
            'sheet': '',
            'label': 'Variación anual del acumulado en lo que va de año. De 80 a 84 años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-80-84.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_85_mas': {
            'sheet': '',
            'label': 'Variación anual del acumulado en lo que va de año. De 85 y más años',
            'category': 'Mortalidad edades',
            'variables': [
                '',
                ''],
            'moving_avg': [
                '',
                ''
            ],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''},
                'Cantabria_MM': {'decimals': 0, 'label': ''},
                'España_MM': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-85-mas.json-stat'
        }
    },
    'globals': {
        'csv': 'vision-global-defunciones-semana.csv'
    }
}

deaths_week_cfg = Baseconfig(params)
deaths_week_cfg.add(common_cfg)
