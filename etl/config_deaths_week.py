from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_semanal_demo.xlsx',
    'series': {
        'mortalidad_total_base': {
            'sheet': 'Defunciones semanas',
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
            'sheet': 'Defunciones semanas',
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
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual del acumulado en lo que va de año',
            'category': 'Mortalidad total',
            'variables': [
                'Variación anual del acumulado en lo que va de año_Canatbria',
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
            'sheet': 'Defunciones semanas',
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
            'sheet': 'Defunciones semanas',
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
            'sheet': 'Defunciones semanas',
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
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual del acumulado en lo que va de año. Hombres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Variación anual del acumulado en lo que va de año_Canatbria_Hombres',
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
            'sheet': 'Defunciones semanas',
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
            'sheet': 'Defunciones semanas',
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
            'sheet': 'Defunciones semanas',
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
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual del acumulado en lo que va de año. Mujeres',
            'category': 'Mortalidad por sexos',
            'variables': [
                'Variación anual del acumulado en lo que va de año_Canatbria_Mujeres',
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
            'sheet': 'Defunciones semanas',
            'label': 'Dato base. Dato base. Hasta 64 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Dato base. Hasta 64 años_Cantabria',
                'Dato base. Hasta 64 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-hasta64.json-stat'
        },
        'mortalidad_edades_base_65_74': {
            'sheet': 'Defunciones semanas',
            'label': 'Dato base. Dato base. De 65 a 74 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Dato base. De 65 a 74 años_Cantabria',
                'Dato base. De 65 a 74 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-65-74.json-stat'
        },
        'mortalidad_edades_base_75_79': {
            'sheet': 'Defunciones semanas',
            'label': 'Dato base. Dato base. De 75 a 79 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Dato base. De 75 a 79 años_Cantabria',
                'Dato base. De 75 a 79 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-75-79.json-stat'
        },
        'mortalidad_edades_base_80_84': {
            'sheet': 'Defunciones semanas',
            'label': 'Dato base. Dato base. De 80 a 84 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Dato base. De 80 a 84 años_Cantabria',
                'Dato base. De 80 a 84 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-80-84.json-stat'
        },
        'mortalidad_edades_base_85_mas': {
            'sheet': 'Defunciones semanas',
            'label': 'Dato base. Dato base. De 85 y más años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Dato base. De 85 y más años_Cantabria',
                'Dato base. De 85 y más años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-base-85-mas.json-stat'
        },
        'mortalidad_edades_acumulado_hasta64': {
            'sheet': 'Defunciones semanas',
            'label': 'Acumulado en lo que va de año. Dato base. Hasta 64 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Acumulado en lo que va de año. Hasta 64 años_Cantabria',
                'Acumulado en lo que va de año. Hasta 64 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-hasta64.json-stat'
        },
        'mortalidad_edades_acumulado_65_74': {
            'sheet': 'Defunciones semanas',
            'label': 'Acumulado en lo que va de año. Dato base. De 65 a 74 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Acumulado en lo que va de año. De 65 a 74 años_Cantabria',
                'Acumulado en lo que va de año. De 65 a 74 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-65-74.json-stat'
        },
        'mortalidad_edades_acumulado_75_79': {
            'sheet': 'Defunciones semanas',
            'label': 'Acumulado en lo que va de año. Dato base. De 75 a 79 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Acumulado en lo que va de año. De 75 a 79 años_Cantabria',
                'Acumulado en lo que va de año. De 75 a 79 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-75-79.json-stat'
        },
        'mortalidad_edades_acumulado_80_84': {
            'sheet': 'Defunciones semanas',
            'label': 'Acumulado en lo que va de año. Dato base. De 80 a 84 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Acumulado en lo que va de año. De 80 a 84 años_Cantabria',
                'Acumulado en lo que va de año. De 80 a 84 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-80-84.json-stat'
        },
        'mortalidad_edades_acumulado_85_mas': {
            'sheet': 'Defunciones semanas',
            'label': 'Acumulado en lo que va de año. Dato base. De 85 y más años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Acumulado en lo que va de año. De 85 y más años_Cantabria',
                'Acumulado en lo que va de año. De 85 y más años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-acumulado-85-mas.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado_hasta64': {
            'sheet': 'Defunciones semanas',
            'label': 'Diferencia absoluta del acumulado. Dato base. Hasta 64 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Diferencia absoluta del acumulado. Hasta 64 años_Cantabria',
                'Diferencia absoluta del acumulado. Hasta 64 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado-hasta64.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado_65_74': {
            'sheet': 'Defunciones semanas',
            'label': 'Diferencia absoluta del acumulado. Dato base. De 65 a 74 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Diferencia absoluta del acumulado. De 65 a 74 años_Cantabria',
                'Diferencia absoluta del acumulado. De 65 a 74 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado-65-74.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado_75_79': {
            'sheet': 'Defunciones semanas',
            'label': 'Diferencia absoluta del acumulado. Dato base. De 75 a 79 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Diferencia absoluta del acumulado. De 75 a 79 años_Cantabria',
                'Diferencia absoluta del acumulado. De 75 a 79 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado-75-79.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado_80_84': {
            'sheet': 'Defunciones semanas',
            'label': 'Diferencia absoluta del acumulado. Dato base. De 80 a 84 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Diferencia absoluta del acumulado. De 80 a 84 años_Cantabria',
                'Diferencia absoluta del acumulado. De 80 a 84 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado-80-84.json-stat'
        },
        'mortalidad_edades_diferencia_acumulado_85_mas': {
            'sheet': 'Defunciones semanas',
            'label': 'Diferencia absoluta del acumulado. Dato base. De 85 y más años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Diferencia absoluta del acumulado. De 85 y más años_Cantabria',
                'Diferencia absoluta del acumulado. De 85 y más años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-diferencia-acumulado-85-mas.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_hasta64': {
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual del acumulado en lo que va de año. Dato base. Hasta 64 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Variación anual del acumulado en lo que va de año. Hasta 64 años_Cantabria',
                'Variación anual del acumulado en lo que va de año. Hasta 64 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-hasta64.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_65_74': {
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual del acumulado en lo que va de año. Dato base. De 65 a 74 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Variación anual del acumulado en lo que va de año. De 65 a 74 años_Cantabria',
                'Variación anual del acumulado en lo que va de año. De 65 a 74 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-65-74.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_75_79': {
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual del acumulado en lo que va de año. Dato base. De 75 a 79 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Variación anual del acumulado en lo que va de año. De 75 a 79 años_Cantabria',
                'Variación anual del acumulado en lo que va de año. De 75 a 79 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-75-79.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_80_84': {
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual del acumulado en lo que va de año. Dato base. De 80 a 84 años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Variación anual del acumulado en lo que va de año. De 80 a 84 años_Cantabria',
                'Variación anual del acumulado en lo que va de año. De 80 a 84 años_España'],
            'source': '',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': ''}
            },
            'note': [''],
            'json': 'mortalidad-edades-variacion-acumulado-80-84.json-stat'
        },
        'mortalidad_edades_variacion_acumulado_85_mas': {
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual del acumulado en lo que va de año. Dato base. De 85 y más años_Cantabria',
            'category': 'Mortalidad edades',
            'variables': [
                'Variación anual del acumulado en lo que va de año. De 85 y más años_Cantabria',
                'Variación anual del acumulado en lo que va de año. De 85 y más años_España'],
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
    },
    'widgets': {
        'defunciones_sexo': {
            'sheet': 'Defunciones semanas',
            'label': 'Defunciones Estimadas por sexo. 2020',
            'variables': [
                'Dato base_Cantabria_Hombres',
                'Dato base_Cantabria_Mujeres',
                'Dato base_Cantabria',
                'Dato base_España_Hombres',
                'Dato base_España_Mujeres',
                'Dato base_España'],
            'source': '',
            'unit':{
                'Dato base_Cantabria_Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'Dato base_Cantabria_Mujeres': {'decimals': 0, 'label': 'Defunciones'},
                'Dato base_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Dato base_España_Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'Dato base_España_Mujeres': {'decimals': 0, 'label': 'Defunciones'},
                'Dato base_España': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'defunciones-sexo.json-stat'
        },
        'defunciones_acumuladas_sexo': {
            'sheet': 'Defunciones semanas',
            'label': 'Defunciones Estimadas acumuladas por sexo. 2020',
            'variables': [
                'Acumulado en lo que va de año_Cantabria_Hombres',
                'Acumulado en lo que va de año_Cantabria_Mujeres',
                'Acumulado en lo que va de año_Cantabria',
                'Acumulado en lo que va de año_España_Hombres',
                'Acumulado en lo que va de año_España_Mujeres',
                'Acumulado en lo que va de año_España'],
            'source': '',
            'unit':{
                'Acumulado en lo que va de año_Cantabria_Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'Acumulado en lo que va de año_Cantabria_Mujeres': {'decimals': 0, 'label': 'Defunciones'},
                'Acumulado en lo que va de año_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Acumulado en lo que va de año_España_Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'Acumulado en lo que va de año_España_Mujeres': {'decimals': 0, 'label': 'Defunciones'},
                'Acumulado en lo que va de año_España': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'defunciones-acumuladas-sexo.json-stat'
        },
        'defunciones_acumuladas_variacion_anual_sexo': {
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual Defunciones Estimadas acumuladas por sexo. 2020',
            'variables': [
                'Variación anual del acumulado en lo que va de año_Canatbria_Hombres',
                'Variación anual del acumulado en lo que va de año_Canatbria_Mujeres',
                'Variación anual del acumulado en lo que va de año_Canatbria',
                'Variación anual del acumulado en lo que va de año_España_Hombres',
                'Variación anual del acumulado en lo que va de año_España_Mujeres',
                'Variación anual del acumulado en lo que va de año_España'],
            'source': '',
            'unit':{
                'Variación anual del acumulado en lo que va de año_Canatbria_Hombres': {'decimals': 0, 'label': '%'},
                'Variación anual del acumulado en lo que va de año_Canatbria_Mujeres': {'decimals': 0, 'label': '%'},
                'Variación anual del acumulado en lo que va de año_Canatbria': {'decimals': 0, 'label': '%'},
                'Variación anual del acumulado en lo que va de año_España_Hombres': {'decimals': 0, 'label': '%'},
                'Variación anual del acumulado en lo que va de año_España_Mujeres': {'decimals': 0, 'label': '%'},
                'Variación anual del acumulado en lo que va de año_España': {'decimals': 0, 'label': '%'}
            },
            'note': [''],
            'json': 'defunciones-acumuladas-variacion-anual-sexo.json-stat'
        },
        'defunciones_grupos_edad_cantabria': {
            'sheet': 'Defunciones semanas',
            'label': 'Defunciones Estimadas por grupos de edad. Cantabria. 2020',
            'variables': [
                'Dato base. Hasta 64 años_Cantabria',
                'Dato base. De 65 a 74 años_Cantabria',
                'Dato base. De 75 a 79 años_Cantabria',
                'Dato base. De 80 a 84 años_Cantabria',
                'Dato base. De 85 y más años_Cantabria'],
            'source': '',
            'unit':{
                'Dato base. Hasta 64 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Dato base. De 65 a 74 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Dato base. De 75 a 79 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Dato base. De 80 a 84 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Dato base. De 85 y más años_Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': ['No se incluyen los datos de edad desconocida'],
            'json': 'defunciones-grupos-edad-cantabria.json-stat'
        },
        'defunciones_acumuladas_grupos_edad_cantabria': {
            'sheet': 'Defunciones semanas',
            'label': 'Defunciones Estimadas acumuladas por grupos de edad. Cantabria. 2020',
            'variables': [
                'Acumulado en lo que va de año. Hasta 64 años_Cantabria',
                'Acumulado en lo que va de año. De 65 a 74 años_Cantabria',
                'Acumulado en lo que va de año. De 75 a 79 años_Cantabria',
                'Acumulado en lo que va de año. De 80 a 84 años_Cantabria',
                'Acumulado en lo que va de año. De 85 y más años_Cantabria'],
            'source': '',
            'unit':{
                'Acumulado en lo que va de año. Hasta 64 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Acumulado en lo que va de año. De 65 a 74 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Acumulado en lo que va de año. De 75 a 79 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Acumulado en lo que va de año. De 80 a 84 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Acumulado en lo que va de año. De 85 y más años_Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': ['No se incluyen los datos de edad desconocida'],
            'json': 'defunciones-acumuladas-grupos-edad-cantabria.json-stat'
        },
        'defunciones_acumuladas_grupos_edad_cantabria_variacion_anual': {
            'sheet': 'Defunciones semanas',
            'label': 'Variación anual Defunciones Estimadas acumuladas por grupos de edad. Cantabria. 2020',
            'variables': [
                'Variación anual del acumulado en lo que va de año. Hasta 64 años_Cantabria',
                'Variación anual del acumulado en lo que va de año. De 65 a 74 años_Cantabria',
                'Variación anual del acumulado en lo que va de año. De 75 a 79 años_Cantabria',
                'Variación anual del acumulado en lo que va de año. De 80 a 84 años_Cantabria',
                'Variación anual del acumulado en lo que va de año. De 85 y más años_Cantabria'],
            'source': '',
            'unit':{
                'Variación anual del acumulado en lo que va de año. Hasta 64 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Variación anual del acumulado en lo que va de año. De 65 a 74 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Variación anual del acumulado en lo que va de año. De 75 a 79 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Variación anual del acumulado en lo que va de año. De 80 a 84 años_Cantabria': {'decimals': 0, 'label': 'Defunciones'},
                'Variación anual del acumulado en lo que va de año. De 85 y más años_Cantabria': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': ['No se incluyen los datos de edad desconocida'],
            'json': 'defunciones-acumuladas-grupos-edad-cantabria-variacion-anual.json-stat'
        }
    },
    'graphs': {
    }
}

deaths_week_cfg = Baseconfig(params)
deaths_week_cfg.add(common_cfg)
