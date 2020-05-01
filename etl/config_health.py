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
        'camas_instaladas': {
            'sheet': 'Dotación hospitales',
            'label': 'Camas instaladas por 1.000 hab',
            'category': 'Dotación hospitales',
            'variables': [
                'Camas instaladas por 1.000 hab_Cantabria',
                'Camas instaladas por 1.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por mil'},
                'España': {'decimals': 2, 'label': 'Tanto por mil'}
            },
            'note': [''],
            'json': 'camas-instaladas.json-stat'
        },
        'camas_funcionamiento': {
            'sheet': 'Dotación hospitales',
            'label': 'Camas en funcionamiento por 1.000 hab',
            'category': 'Dotación hospitales',
            'variables': [
                'Camas en funcionamiento por 1.000 hab_Cantabria',
                'Camas en funcionamiento por 1.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por mil'},
                'España': {'decimals': 2, 'label': 'Tanto por mil'}
            },
            'note': [''],
            'json': 'camas-funcionamiento.json-stat'
        },
        'camas_agudos': {
            'sheet': 'Dotación hospitales',
            'label': 'Camas de agudos por 1.000 hab',
            'category': 'Dotación hospitales',
            'variables': [
                'Camas de agudos por 1.000 hab_Cantabria',
                'Camas de agudos por 1.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por mil'},
                'España': {'decimals': 2, 'label': 'Tanto por mil'}
            },
            'note': [''],
            'json': 'camas-agudos.json-stat'
        },
        'quirofanos': {
            'sheet': 'Dotación hospitales',
            'label': 'Quirófanos por 1.000 hab',
            'category': 'Dotación hospitales',
            'variables': [
                'Quirófanos por 1.000 hab_Cantabria',
                'Quirófanos por 1.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por mil'},
                'España': {'decimals': 2, 'label': 'Tanto por mil'}
            },
            'note': [''],
            'json': 'quirofanos.json-stat'
        },
        'hospital_dia': {
            'sheet': 'Dotación hospitales',
            'label': 'Total Puestos Hospital de Día por 100.000 hab',
            'category': 'Dotación hospitales',
            'variables': [
                'Total Puestos Hospital de Día por 100.000 hab_Cantabria',
                'Total Puestos Hospital de Día por 100.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'hospital-dia.json-stat'
        },
        'camas_instaladas_publicos': {
            'sheet': 'Dotación hospitales',
            'label': 'Camas instaladas por 1.000 hab. Hospitales públicos',
            'category': 'Dotación hospitales publicos',
            'variables': [
                'HOSP_PUB_Camas instaladas por 1.000 hab_Cantabria',
                'HOSP_PUB_Camas instaladas por 1.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por mil'},
                'España': {'decimals': 2, 'label': 'Tanto por mil'}
            },
            'note': [''],
            'json': 'camas-instaladas-publicos.json-stat'
        },
        'camas_funcionamiento_publicos': {
            'sheet': 'Dotación hospitales',
            'label': 'Camas en funcionamiento por 1.000 hab.Hospitales públicos',
            'category': 'Dotación hospitales publicos',
            'variables': [
                'HOSP_PUB_Camas en funcionamiento por 1.000 hab_Cantabria',
                'HOSP_PUB_Camas en funcionamiento por 1.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por mil'},
                'España': {'decimals': 2, 'label': 'Tanto por mil'}
            },
            'note': [''],
            'json': 'camas-funcionamiento-publicos.json-stat'
        },
        'camas_agudos_publicos': {
            'sheet': 'Dotación hospitales',
            'label': 'Camas de agudos por 1.000 hab. Hospitales públicos',
            'category': 'Dotación hospitales publicos',
            'variables': [
                'HOSP_PUB_Camas de agudos por 1.000 hab_Cantabria',
                'HOSP_PUB_Camas de agudos por 1.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por mil'},
                'España': {'decimals': 2, 'label': 'Tanto por mil'}
            },
            'note': [''],
            'json': 'camas-agudos-publicos.json-stat'
        },
        'quirofanos_publicos': {
            'sheet': 'Dotación hospitales',
            'label': 'Quirófanos por 1.000 hab. Hospitales públicos',
            'category': 'Dotación hospitales publicos',
            'variables': [
                'HOSP_PUB_Quirófanos por 1.000 hab_Cantabria',
                'HOSP_PUB_Quirófanos por 1.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por mil'},
                'España': {'decimals': 2, 'label': 'Tanto por mil'}
            },
            'note': [''],
            'json': 'quirofanos-publicos.json-stat'
        },
        'hospital_dia_publicos': {
            'sheet': 'Dotación hospitales',
            'label': 'Total Puestos Hospital de Día por 100.000 hab. Hospitales públicos',
            'category': 'Dotación hospitales publicos',
            'variables': [
                'HOSP_PUB_Total Puestos Hospital de Día por 100.000 hab_Cantabria',
                'HOSP_PUB_Total Puestos Hospital de Día por 100.000 hab_España'],
            'source': 'ICANE a partir de Estadística de Centros Sanitarios de Atención Especializada, Ministerio de Sanidad',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'hospital-dia-publicos.json-stat'
        },
        'morbilidad_neumonia': {
            'sheet': 'Tasas_Morbilidad_hospitalaria',
            'label': 'Tasa de morbilidad Neumonía por 100.000 hab',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Tasas de Morbilidad Hospitalaria por 100.000 habitantes_Neumonía_Cantabria',
                'Tasas de Morbilidad Hospitalaria por 100.000 habitantes_Neumonía_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'morbilidad-neumonia.json-stat'
        },
        'morbilidad_neumonia_hombres': {
            'sheet': 'Tasas_Morbilidad_hospitalaria',
            'label': 'Tasa de morbilidad Neumonía por 100.000 hab. Hombres',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Tasas de Morbilidad Hospitalaria por 100.000 Hombres_Neumonía_Cantabria',
                'Tasas de Morbilidad Hospitalaria por 100.000 Hombres_Neumonía_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'morbilidad-neumonia-hombres.json-stat'
        },
        'morbilidad_neumonia_mujeres': {
            'sheet': 'Tasas_Morbilidad_hospitalaria',
            'label': 'Tasa de morbilidad Neumonía por 100.000 hab. Mujeres',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Tasas de Morbilidad Hospitalaria por 100.000 Mujeres_Neumonía_Cantabria',
                'Tasas de Morbilidad Hospitalaria por 100.000 Mujeres_Neumonía_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'morbilidad-neumonia-mujeres.json-stat'
        },
        'morbilidad': {
            'sheet': 'Tasas_Morbilidad_hospitalaria',
            'label': 'Tasa de morbilidad por 100.000 hab',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Tasas de Morbilidad Hospitalaria por 100.000 habitantes_Cantabria',
                'Tasas de Morbilidad Hospitalaria por 100.000 habitantes_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'morbilidad.json-stat'
        },
        'morbilidad_hombres': {
            'sheet': 'Tasas_Morbilidad_hospitalaria',
            'label': 'Tasa de morbilidad por 100.000 hab. Hombres',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Tasas de Morbilidad Hospitalaria por 100.000 Hombres_Cantabria',
                'Tasas de Morbilidad Hospitalaria por 100.000 Hombres_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'morbilidad-hombres.json-stat'
        },
        'morbilidad_mujeres': {
            'sheet': 'Tasas_Morbilidad_hospitalaria',
            'label': 'Tasa de morbilidad por 100.000 hab. Mujeres',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Tasas de Morbilidad Hospitalaria por 100.000 Mujeres_Cantabria',
                'Tasas de Morbilidad Hospitalaria por 100.000 Mujeres_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 2, 'label': 'Tanto por cienmil'}
            },
            'note': [''],
            'json': 'morbilidad-mujeres.json-stat'
        },
        'estancia_neumonia': {
            'sheet': 'Estancia_media',
            'label': 'Neumonía. Estancia media en días',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Estancia_media_Neumonía_Cantabria',
                'Estancia_media_Neumonía_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Días'},
                'España': {'decimals': 2, 'label': 'Días'}
            },
            'note': [''],
            'json': 'estancia-neumonia.json-stat'
        },
        'estancia_neumonia_hombres': {
            'sheet': 'Estancia_media',
            'label': 'Neumonía. Estancia media en días. Hombres',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Estancia_media_Hombres_Neumonía_Cantabria',
                'Estancia_media_Hombres_Neumonía_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Días'},
                'España': {'decimals': 2, 'label': 'Días'}
            },
            'note': [''],
            'json': 'estancia-neumonia-hombres.json-stat'
        },
        'estancia_neumonia_mujeres': {
            'sheet': 'Estancia_media',
            'label': 'Neumonía. Estancia media en días. Mujeres',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Estancia_media_Mujeres_Neumonía_Cantabria',
                'Estancia_media_Mujeres_Neumonía_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'í'},
                'España': {'decimals': 2, 'label': 'Días'}
            },
            'note': [''],
            'json': 'estancia-neumonia-mujeres.json-stat'
        },
        'estancia': {
            'sheet': 'Estancia_media',
            'label': 'Estancia media',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Estancia_media_Cantabria',
                'Estancia_media_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Días'},
                'España': {'decimals': 2, 'label': 'í'}
            },
            'note': [''],
            'json': 'estancia.json-stat'
        },
        'estancia_hombres': {
            'sheet': 'Estancia_media',
            'label': 'Estancia media Hombres',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Estancia_media_Hombres_Cantabria',
                'Estancia_media_Hombres_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Días'},
                'España': {'decimals': 2, 'label': 'Días'}
            },
            'note': [''],
            'json': 'estancia-hombres.json-stat'
        },
        'estancia_mujeres': {
            'sheet': 'Estancia_media',
            'label': 'Estancia media Mujeres',
            'category': 'Morbilidad hospitalaria',
            'variables': [
                'Estancia_media_Mujeres_Cantabria',
                'Estancia_media_Mujeres_España'],
            'source': 'ICANE a partir de Estadística de Morbilidad Hospitalaria, INE',
            'unit':{
                'Cantabria': {'decimals': 2, 'label': 'Días'},
                'España': {'decimals': 2, 'label': 'Días'}
            },
            'note': [''],
            'json': 'estancia-mujeres.json-stat'
        }
    },
    'globals': {
        'csv': 'vision-global-salud.csv'
    }
}

health_cfg = Baseconfig(params)
health_cfg.add(common_cfg)
