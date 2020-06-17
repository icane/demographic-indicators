from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_semanal_demo_gráficos.xlsx',
    'series': {
        'mortalidad_total_base': {
            'sheet': 'Datos',
            'label': 'Dato base',
            'category': 'Mortalidad total',
            'variables': [
                'Dato base_Cantabria',
                'Dato base_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-total-base.json-stat'
        },
        'mortalidad_total_acumulado': {
            'sheet': 'Datos',
            'label': 'Acumulado en lo que va de año',
            'category': 'Mortalidad total',
            'variables': [
                'Acumulado en lo que va de año_Cantabria',
                'Acumulado en lo que va de año_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-total-acumulado.json-stat'
        },
        'mortalidad_total_variacion_acumulado': {
            'sheet': 'Datos',
            'label': 'Variación anual del acumulado en lo que va de año',
            'category': 'Mortalidad total',
            'variables': [
                'Variación anual del acumulado en lo que va de año_Cantabria',
                'Variación anual del acumulado en lo que va de año_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-total-variacion-acumulado.json-stat'
        },
        'mortalidad_sexo_dato_base_hombres': {
            'sheet': 'Datos',
            'label': 'Dato base. Hombres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Dato base_Cantabria_Hombres',
                'Dato base_España_Hombres'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-dato-base-hombres.json-stat'
        },
        'mortalidad_sexo_acumulado_hombres': {
            'sheet': 'Datos',
            'label': 'Acumulado en lo que va de año. Hombres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Acumulado en lo que va de año_Cantabria_Hombres',
                'Acumulado en lo que va de año_España_Hombres'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-acumulado-hombres.json-stat'
        },
        'mortalidad_sexo_diferencia_acumulado_hombres': {
            'sheet': 'Datos',
            'label': 'Diferencia absoluta del acumulado. Hombres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Diferencia absoluta del acumulado_Cantabria_Hombres',
                'Diferencia absoluta del acumulado_España_Hombres'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-diferencia-acumulado-hombres.json-stat'
        },
        'mortalidad_sexo_variacion_anual_acumulado_hombres': {
            'sheet': 'Datos',
            'label': 'Variación anual del acumulado en lo que va de año. Hombres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Variación anual del acumulado en lo que va de año_Cantabria_Hombres',
                'Variación anual del acumulado en lo que va de año_España_Hombres'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-variacion-anual-acumulado-hombres.json-stat'
        },
        'mortalidad_sexo_dato_base_mujeres': {
            'sheet': 'Datos',
            'label': 'Dato base. Mujeres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Dato base_Cantabria_Mujeres',
                'Dato base_España_Mujeres'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-dato-base-mujeres.json-stat'
        },
        'mortalidad_sexo_acumulado_mujeres': {
            'sheet': 'Datos',
            'label': 'Acumulado en lo que va de año. Mujeres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Acumulado en lo que va de año_Cantabria_Mujeres',
                'Acumulado en lo que va de año_España_Mujeres'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-acumulado-mujeres.json-stat'
        },
        'mortalidad_sexo_diferencia_acumulado_mujeres': {
            'sheet': 'Datos',
            'label': 'Diferencia absoluta del acumulado. Mujeres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Diferencia absoluta del acumulado_Cantabria_Mujeres',
                'Diferencia absoluta del acumulado_España_Mujeres'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-diferencia-acumulado-mujeres.json-stat'
        },
        'mortalidad_sexo_variacion_anual_acumulado_mujeres': {
            'sheet': 'Datos',
            'label': 'Variación anual del acumulado en lo que va de año. Mujeres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Variación anual del acumulado en lo que va de año_Cantabria_Mujeres',
                'Variación anual del acumulado en lo que va de año_España_Mujeres'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''},
                'España': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-sexo-variacion-anual-acumulado-mujeres.json-stat'
        },
        'mortalidad_edades_base_hasta64': {
            'sheet': 'Datos',
            'label': 'Dato base. Hasta 64 años',
            'category': 'Mortalidad edades',
            'variables': ['Hasta 64 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-hasta64.json-stat'
        },
        'mortalidad_edades_base_65_74': {
            'sheet': 'Datos',
            'label': 'Dato base. De 65 a 74 años',
            'category': 'Mortalidad edades',
            'variables': ['65-74 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-65-74.json-stat'
        },
        'mortalidad_edades_base_75_79': {
            'sheet': 'Datos',
            'label': 'Dato base. De 75 a 79 años',
            'category': 'Mortalidad edades',
            'variables': ['De 75 a 79 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-75-79.json-stat'
        },
        'mortalidad_edades_base_80_84': {
            'sheet': 'Datos',
            'label': 'Dato base. De 80 a 84 años',
            'category': 'Mortalidad edades',
            'variables': ['De 80 a 84 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-80-84.json-stat'
        },
        'mortalidad_edades_base_85_mas': {
            'sheet': 'Datos',
            'label': 'Dato base. De 85 y más años',
            'category': 'Mortalidad edades',
            'variables': ['De 85 y +_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-85-mas.json-stat'
        },
        'mortalidad_edades_acumulado_hasta64': {
            'sheet': 'Datos',
            'label': 'Acumulado en lo que va de año. Hasta 64 años',
            'category': 'Mortalidad edades',
            'variables': ['Acumulado_Hasta 64 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-hasta64.json-stat'
        },
        'mortalidad_edades_acumulado_65_74': {
            'sheet': 'Datos',
            'label': 'Acumulado en lo que va de año. De 65 a 74 años',
            'category': 'Mortalidad edades',
            'variables': ['Acumulado_65-74 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-65-74.json-stat'
        },
        'mortalidad_edades_acumulado_75_79': {
            'sheet': 'Datos',
            'label': 'Acumulado en lo que va de año. De 75 a 79 años',
            'category': 'Mortalidad edades',
            'variables': ['Acumulado_De 75 a 79 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-75-79.json-stat'
        },
        'mortalidad_edades_acumulado_80_84': {
            'sheet': 'Datos',
            'label': 'Acumulado en lo que va de año. De 80 a 84 años',
            'category': 'Mortalidad edades',
            'variables': ['Acumulado_De 80 a 84 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-80-84.json-stat'
        },
        'mortalidad_edades_acumulado_85_mas': {
            'sheet': 'Datos',
            'label': 'Acumulado en lo que va de año. De 85 y más años',
            'category': 'Mortalidad edades',
            'variables': ['Acumulado_De 85 y +_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-85-mas.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_hasta64': {
            'sheet': 'Datos',
            'label': 'Variación anual del acumulado en lo que va de año. Hasta 64 años',
            'category': 'Mortalidad edades',
            'variables': ['Variación anual acumulado_Hasta 64 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-hasta64.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_65_74': {
            'sheet': 'Datos',
            'label': 'Variación anual del acumulado en lo que va de año. De 65 a 74 años',
            'category': 'Mortalidad edades',
            'variables': ['Variación anual acumulado_65-74 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-65-74.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_75_79': {
            'sheet': 'Datos',
            'label': 'Variación anual del acumulado en lo que va de año. De 75 a 79 años',
            'category': 'Mortalidad edades',
            'variables': ['Variación anual acumulado_De 75 a 79 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-75-79.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_80_84': {
            'sheet': 'Datos',
            'label': 'Variación anual del acumulado en lo que va de año. De 80 a 84 años',
            'category': 'Mortalidad edades',
            'variables': ['Variación anual acumulado_De 80 a 84 años_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-80-84.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_85_mas': {
            'sheet': 'Datos',
            'label': 'Variación anual del acumulado en lo que va de año. De 85 y más años',
            'category': 'Mortalidad edades',
            'variables': ['Variación anual acumulado_De 85 y +_Cantabria'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
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
