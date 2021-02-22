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
            'label': 'Dato base. Hasta 64 años',
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
            'label': 'Dato base. De 65 a 74 años',
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
            'label': 'Dato base. De 75 a 79 años',
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
            'label': 'Dato base. De 80 a 84 años',
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
            'label': 'Dato base. De 85 y más años',
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
            'label': 'Acumulado en lo que va de año. Hasta 64 años',
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
            'label': 'Acumulado en lo que va de año. De 65 a 74 años',
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
            'label': 'Acumulado en lo que va de año. De 75 a 79 años',
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
            'label': 'Acumulado en lo que va de año. De 80 a 84 años',
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
            'label': 'Acumulado en lo que va de año. De 85 y más años',
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
            'label': 'Diferencia absoluta del acumulado. Hasta 64 años',
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
            'label': 'Diferencia absoluta del acumulado. De 65 a 74 años',
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
            'label': 'Diferencia absoluta del acumulado. De 75 a 79 años',
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
            'label': 'Diferencia absoluta del acumulado. De 80 a 84 años',
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
            'label': 'Diferencia absoluta del acumulado. De 85 y más años',
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
            'label': 'Variación anual del acumulado en lo que va de año. Hasta 64 años',
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
            'label': 'Variación anual del acumulado en lo que va de año. De 65 a 74 años',
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
            'label': 'Variación anual del acumulado en lo que va de año. De 75 a 79 años',
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
            'label': 'Variación anual del acumulado en lo que va de año. De 80 a 84 años',
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
            'label': 'Variación anual del acumulado en lo que va de año. De 85 y más años',
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
            'sheet': 'Defunciones sexo',
            'label': 'Defunciones Estimadas por sexo. 2020',
            'variables': [
                'Cantabria_Hombres',
                'Cantabria_Mujeres',
                'Cantabria_Total',
                'España_Hombres',
                'España_Mujeres',
                'España_Total'],
            'source': '',
            'unit':{
                'Cantabria_Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'Cantabria_Mujeres': {'decimals': 0, 'label': 'Defunciones'},
                'Cantabria_Total': {'decimals': 0, 'label': 'Defunciones'},
                'España_Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'España_Mujeres': {'decimals': 0, 'label': 'Defunciones'},
                'España_Total': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'defunciones-sexo.json-stat'
        },
        'defunciones_acumuladas_sexo': {
            'sheet': 'Defunciones acumuladas sexo',
            'label': 'Defunciones Estimadas acumuladas por sexo. 2020',
            'variables': [
                'Cantabria_Hombres',
                'Cantabria_Mujeres',
                'Cantabria_Total',
                'España_Hombres',
                'España_Mujeres',
                'España_Total'],
            'source': '',
            'unit':{
                'Cantabria_Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'Cantabria_Mujeres': {'decimals': 0, 'label': 'Defunciones'},
                'Cantabria_Total': {'decimals': 0, 'label': 'Defunciones'},
                'España_Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'España_Mujeres': {'decimals': 0, 'label': 'Defunciones'},
                'España_Total': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'defunciones-acumuladas-sexo.json-stat'
        },
        'defunciones_acumuladas_variacion_anual_sexo': {
            'sheet': 'Defunciones acumuladas variación anual sexo',
            'label': 'Variación anual Defunciones Estimadas acumuladas por sexo. 2020',
            'variables': [
                'Cantabria_Hombres',
                'Cantabria_Mujeres',
                'Cantabria_Total',
                'España_Hombres',
                'España_Mujeres',
                'España_Total'],
            'source': '',
            'unit':{
                'Cantabria_Hombres': {'decimals': 0, 'label': '%'},
                'Cantabria_Mujeres': {'decimals': 0, 'label': '%'},
                'Cantabria_Total': {'decimals': 0, 'label': '%'},
                'España_Hombres': {'decimals': 0, 'label': '%'},
                'España_Mujeres': {'decimals': 0, 'label': '%'},
                'España_Total': {'decimals': 0, 'label': '%'}
            },
            'note': [''],
            'json': 'defunciones-acumuladas-variacion-anual-sexo.json-stat'
        },
        'defunciones_grupos_edad_cantabria': {
            'sheet': 'Defunciones grupos edad',
            'label': 'Defunciones Estimadas por grupos de edad. Cantabria. 2020',
            'variables': [
                'Hasta 64 años',
                'De 65 a 74 años',
                'De 75 a 79 años',
                'De 80 a 84 años',
                'De 85 y más años'],
            'source': '',
            'unit':{
                'Hasta 64 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 65 a 74 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 75 a 79 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 80 a 84 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 85 y más años': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': ['No se incluyen los datos de edad desconocida'],
            'json': 'defunciones-grupos-edad-cantabria.json-stat'
        },
        'defunciones_acumuladas_grupos_edad_cantabria': {
            'sheet': 'Defunciones acumuladas grupos edad',
            'label': 'Defunciones Estimadas acumuladas por grupos de edad. Cantabria. 2020',
            'variables': [
                'Hasta 64 años',
                'De 65 a 74 años',
                'De 75 a 79 años',
                'De 80 a 84 años',
                'De 85 y más años'],
            'source': '',
            'unit':{
                'Hasta 64 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 65 a 74 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 75 a 79 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 80 a 84 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 85 y más años': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': ['No se incluyen los datos de edad desconocida'],
            'json': 'defunciones-acumuladas-grupos-edad-cantabria.json-stat'
        },
        'defunciones_acumuladas_grupos_edad_cantabria_variacion_anual': {
            'sheet': 'Defunciones acumuladas grupos edad variación',
            'label': 'Variación anual Defunciones Estimadas acumuladas por grupos de edad. Cantabria. 2020',
            'variables': [
                'Hasta 64 años',
                'De 65 a 74 años',
                'De 75 a 79 años',
                'De 80 a 84 años',
                'De 85 y más años'],
            'source': '',
            'unit':{
                'Hasta 64 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 65 a 74 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 75 a 79 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 80 a 84 años': {'decimals': 0, 'label': 'Defunciones'},
                'De 85 y más años': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': ['No se incluyen los datos de edad desconocida'],
            'json': 'defunciones-acumuladas-grupos-edad-cantabria-variacion-anual.json-stat'
        }
    },
    'graphs': {
        'defunciones_cantabria': {
            'sheet': 'Defunciones Cantabria Graph',
            'label': 'Defunciones por semana. Cantabria',
            'variables': [
                'Cantabria 2019',
                'Cantabria 2020',
                'Cantabria 2021'],
            'source': '',
            'unit':{
                'Cantabria 2019': {'decimals': 0, 'label': 'Defunciones'},
                'Cantabria 2020': {'decimals': 0, 'label': 'Defunciones'},
                'Cantabria 2021': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'defunciones-cantabria-graph.json-stat'
        },
        'defunciones_acumuladas_cantabria': {
            'sheet': 'Defunciones Acumuladas Cantabria Graph',
            'label': 'Defunciones acumuladas por semana. Cantabria',
            'variables': [
                'Cantabria 2019',
                'Cantabria 2020',
                'Cantabria 2021'],
            'source': '',
            'unit':{
                'Cantabria 2019': {'decimals': 0, 'label': 'Defunciones'},
                'Cantabria 2020': {'decimals': 0, 'label': 'Defunciones'},
                'Cantabria 2021': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'defunciones-acumuladas-cantabria-graph.json-stat'
        },
        'defunciones_cantabria_2020': {
            'sheet': 'Defunciones 2020',
            'label': 'Defunciones por semana Cantabria',
            'variables': [
                'Hombres',
                'Mujeres'],
            'source': '',
            'unit':{
                'Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'Mujeres': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'defunciones-cantabria-2020-graph.json-stat'
        },
        'defunciones_acumuladas_cantabria_2020': {
            'sheet': 'Defunciones acumuladas 2020',
            'label': 'Defunciones acumuladas por semana. Cantabria',
            'variables': [
                'Hombres',
                'Mujeres',
                'Total'],
            'source': '',
            'unit':{
                'Hombres': {'decimals': 0, 'label': 'Defunciones'},
                'Mujeres': {'decimals': 0, 'label': 'Defunciones'},
                'Total': {'decimals': 0, 'label': 'Defunciones'}
            },
            'note': [''],
            'json': 'defunciones-acumuladas-cantabria-2020-graph.json-stat'
        },
        'defunciones_acumuladas_variacion_anual_2019_2020': {
            'sheet': 'Defunciones variación anual acumulado 2019-2020',
            'label': 'Variación anual del acumulado en lo que va de año',
            'variables': [
                'Cantabria 2019',
                'España 2019',
                'Cantabria 2020',
                'España 2020'],
            'source': '',
            'unit':{
                'Cantabria 2019': {'decimals': 0, 'label': '%'},
                'España 2019': {'decimals': 0, 'label': '%'},
                'Cantabria 2020': {'decimals': 0, 'label': '%'},
                'España 2020': {'decimals': 0, 'label': '%'}
            },
            'note': [''],
            'json': 'defunciones-acumuladas-variacion-anual-2019-2020-graph.json-stat'
        },
        'defunciones_acumuladas_variacion_anual_sexo_2020': {
            'sheet': 'Defunciones variación anual acumulado sexo 2020',
            'label': 'Variación anual del acumulado en lo que va de año por sexo. 2020',
            'variables': [
                'España Hombres',
                'España Mujeres',
                'Cantabria Hombres',
                'Cantabria Mujeres'],
            'source': '',
            'unit':{
                'España Hombres': {'decimals': 0, 'label': '%'},
                'España Mujeres': {'decimals': 0, 'label': '%'},
                'Cantabria Hombres': {'decimals': 0, 'label': '%'},
                'Cantabria Mujeres': {'decimals': 0, 'label': '%'}
            },
            'note': [''],
            'json': 'defunciones-acumuladas-variacion-anual-sexo-2020-graph.json-stat'
        }
    }
}

deaths_week_cfg = Baseconfig(params)
deaths_week_cfg.add(common_cfg)
