from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config

params = {
    'file': 'Datos_carga_anuales_demo_final.xlsx',
    'tables': {
        'centros_plazas_usuarios': {
            'sheet': 'Residencial',
            'category': 'Centros, plazas y usuarios',
            'label': 'Centros, plazas y usuarios',
            'variables': [
                'Centros_Cantabria',
                'Centros Residenciales_Cantabria',
                'Vivienda para mayores_Cantabria',
                'Plazas_Cantabria',
                'Plazas_Centros Residenciales_Cantabria',
                'Plazas_Vivienda para mayores_Cantabria',
                'Usuarios_Cantabria',
                'Centros_España',
                'Centros Residenciales_España',
                'Vivienda para mayores_España',
                'Plazas_España',
                'Plazas_Centros Residenciales_España',
                'Plazas_Vivienda para mayores_España',
                'Usuarios_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                '': {'decimals': 0, 'label': 'Centros, Viviendas, Plazas, Usuarios'}},
            'note': [''],
            'json': 'centros-plazas-usuarios.json-stat'
        }
    },
    'series': {
        'indice_cobertura_total': {
            'sheet': 'Residencial',
            'category': 'Índice de Cobertura (nº de plazas/población>=65)*100.',
            'label': 'Total',
            'variables': [],
            'rate_vars': ['Índice de Cobertura_Total_Cantabria', 'Índice de Cobertura_Total_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'indice-cobertura-total.json-stat'},
        'indice_cobertura_centros': {
            'sheet': 'Residencial',
            'category': 'Índice de Cobertura (nº de plazas/población>=65)*100.',
            'label': 'Centros residenciales',
            'variables': [],
            'rate_vars': ['Índice de Cobertura_Centros residenciales_Cantabria', 'Índice de Cobertura_Centros residenciales_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'indice-cobertura-centros.json-stat'},
        'indice_cobertura_viviendas': {
            'sheet': 'Residencial',
            'category': 'Índice de Cobertura (nº de plazas/población>=65)*100.',
            'label': 'Viviendas para mayores',
            'variables': [],
            'rate_vars': ['Índice de Cobertura_Viviendas para mayores_Cantabria', 'Índice de Cobertura_Viviendas para mayores_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'indice-cobertura-viviendas.json-stat'},
        'indice_cobertura_plazas_publica': {
            'sheet': 'Residencial',
            'category': 'Índice de Cobertura (nº de plazas/población>=65)*100.',
            'label': 'Plazas de financiación pública',
            'variables': [],
            'rate_vars': ['Índice de Cobertura_Plazas de financiación pública_Cantabria', 'Índice de Cobertura_Plazas de financiación pública_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'indice-cobertura-plazas-publica.json-stat'},
        'indice_cobertura_plazas_privada': {
            'sheet': 'Residencial',
            'category': 'Índice de Cobertura (nº de plazas/población>=65)*100.',
            'label': 'Plazas de financiación privada',
            'variables': [],
            'rate_vars': ['Índice de Cobertura_Plazas de financiación privada_Cantabria', 'Índice de Cobertura_Plazas de financiación privada_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'indice-cobertura-plazas-privada.json-stat'},
        'indice_cobertura_plazas_publica_residencias': {
            'sheet': 'Residencial',
            'category': 'Índice de Cobertura (nº de plazas/población>=65)*100.',
            'label': 'Plazas de financiación pública. Residencias',
            'variables': [],
            'rate_vars': ['Índice de Cobertura_Plazas de financiación pública. Residencias_Cantabria', 'Índice de Cobertura_Plazas de financiación pública. Residencias_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'indice-cobertura-plazas-publica-residencias.json-stat'},
        'indice_cobertura_plazas_privada_residencias': {
            'sheet': 'Residencial',
            'category': 'Índice de Cobertura (nº de plazas/población>=65)*100.',
            'label': 'Plazas de financiación privada. Residencias',
            'variables': [],
            'rate_vars': ['Índice de Cobertura_Plazas de financiación privada. Residencias_Cantabria', 'Índice de Cobertura_Plazas de financiación privada. Residencias_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'indice-cobertura-plazas-privada-residencias.json-stat'},
        'indice_cobertura_plazas_publica_viviendas': {
            'sheet': 'Residencial',
            'category': 'Índice de Cobertura (nº de plazas/población>=65)*100.',
            'label': 'Plazas de financiación pública.Viviendas',
            'variables': [],
            'rate_vars': ['Índice de Cobertura_Plazas de financiación pública.Viviendas_Cantabria', 'Índice de Cobertura_Plazas de financiación pública.Viviendas_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'indice-cobertura-plazas-publica-viviendas.json-stat'},
        'tasa_ocupacion': {
            'sheet': 'Residencial',
            'category': 'Ocupación',
            'label': 'Tasa de ocupación (usuarios/población>=65)*100.',
            'variables': [],
            'rate_vars': ['Tasa de ocupación_Cantabria', 'Tasa de ocupación_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'tasa-ocupacion.json-stat'},
        'indice_ocupacion': {
            'sheet': 'Residencial',
            'category': 'Ocupación',
            'label': 'Índice de ocupación (usuarios/plazas)*100.',
            'variables': [],
            'rate_vars': ['Índice de ocupación Cantabria', 'Índice de ocupación España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'indice-ocupacion.json-stat'},
        'tamano_medio_centros': {
            'sheet': 'Residencial',
            'category': 'Tamaño medio',
            'label': 'Centros Residenciales. Tamaño medio de los centros (Nº medio de plazas por centro)',
            'variables': [],
            'rate_vars': ['Tamaño medio_Centros Residenciales_Cantabria', 'Tamaño medio_Centros Residenciales_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'tamano-medio-centros.json-stat'},
        'tamano_medio_viviendas': {
            'sheet': 'Residencial',
            'category': 'Tamaño medio',
            'label': 'Viviendas. Tamaño medio de los centros (Nº medio de plazas por centro)',
            'variables': [],
            'rate_vars': ['Tamaño medio_Viviendas_Cantabria', 'Tamaño medio_Viviendas_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'tamano-medio-viviendas.json-stat'},
        'titularidad_centros_publicos': {
            'sheet': 'Residencial',
            'category': 'Titularidad',
            'label': 'Porcentaje Centros públicos',
            'variables': [],
            'rate_vars': ['Porcentaje Centros públicos_Cantabria', 'Porcentaje Centros públicos_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'titularidad-centros-publicos.json-stat'},
        'titularidad_centros_privados': {
            'sheet': 'Residencial',
            'category': 'Titularidad',
            'label': 'Porcentaje Centros privados',
            'variables': [],
            'rate_vars': ['Porcentaje Centros privados_Cantabria', 'Porcentaje Centros privados_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'titularidad-centros-privados.json-stat'},
        'titularidad_plazas_publica': {
            'sheet': 'Residencial',
            'category': 'Titularidad',
            'label': 'Porcentaje plazas de financiación Pública',
            'variables': [],
            'rate_vars': ['Porcentaje plazas de financiación Pública_Cantabria', 'Porcentaje plazas de financiación Pública_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'titularidad-plazas-publica.json-stat'},
        'titularidad_plazas_privada': {
            'sheet': 'Residencial',
            'category': 'Titularidad',
            'label': 'Porcentaje plazas de financiación Privada',
            'variables': [],
            'rate_vars': ['Porcentaje plazas de financiación Privada_Cantabria', 'Porcentaje plazas de financiación Privada_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'titularidad-plazas-privada.json-stat'},
        'porcen_usuarios_hombres': {
            'sheet': 'Residencial',
            'category': 'Distribuciones por edad y sexo. Centros Residenciales',
            'label': 'Porcentaje de usuarios. Hombres',
            'variables': [],
            'rate_vars': ['Porcentaje de usuarios. Hombres_Cantabria', 'Porcentaje de usuarios. Hombres_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'porcen-usuarios-hombres.json-stat'},
        'porcen_usuarios_mujeres': {
            'sheet': 'Residencial',
            'category': 'Distribuciones por edad y sexo. Centros Residenciales',
            'label': 'Porcentaje de usuarios. Mujeres',
            'variables': [],
            'rate_vars': ['Porcentaje de usuarios. Mujeres_Cantabria', 'Porcentaje de usuarios. Mujeres_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'porcen-usuarios-mujeres.json-stat'},
        'porcen_usuarios_65': {
            'sheet': 'Residencial',
            'category': 'Distribuciones por edad y sexo. Centros Residenciales',
            'label': 'Porcentaje usuarios de 65 a 79 sobre total 65 y +',
            'variables': [],
            'rate_vars': ['Porcentaje usuarios de 65 a 79 sobre total 65 y +_Cantabria', 'Porcentaje usuarios de 65 a 79 sobre total 65 y +_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'porcen-usuarios-65.json-stat'},
        'porcen_usuarios_65_hombres': {
            'sheet': 'Residencial',
            'category': 'Distribuciones por edad y sexo. Centros Residenciales',
            'label': 'Porcentaje usuarios de 65 a 79 sobre total 65 y +. Hombres',
            'variables': [],
            'rate_vars': ['Porcentaje usuarios de 65 a 79 sobre total 65 y +. Hombres_Cantabria', 'Porcentaje usuarios de 65 a 79 sobre total 65 y +. Hombres_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'porcen-usuarios-65-hombres.json-stat'},
        'porcen_usuarios_65_mujeres': {
            'sheet': 'Residencial',
            'category': 'Distribuciones por edad y sexo. Centros Residenciales',
            'label': 'Porcentaje usuarios de 65 a 79 sobre total 65 y +. Mujeres',
            'variables': [],
            'rate_vars': ['Porcentaje usuarios de 65 a 79 sobre total 65 y +. Mujeres_Cantabria', 'Porcentaje usuarios de 65 a 79 sobre total 65 y +. Mujeres_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'porcen-usuarios-65-mujeres.json-stat'},
        'porcen_usuarios_80': {
            'sheet': 'Residencial',
            'category': 'Distribuciones por edad y sexo. Centros Residenciales',
            'label': 'Porcentaje usuarios de 80 año y más sobre total 65 y +',
            'variables': [],
            'rate_vars': ['Porcentaje usuarios de 80 año y más sobre total 65 y +_Cantabria', 'Porcentaje usuarios de 80 año y más sobre total 65 y +_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'porcen-usuarios-80.json-stat'},
        'porcen_usuarios_80_hombres': {
            'sheet': 'Residencial',
            'category': 'Distribuciones por edad y sexo. Centros Residenciales',
            'label': 'Porcentaje usuarios de 80 años y más sobre total 65 y +. Hombres',
            'variables': [],
            'rate_vars': ['Porcentaje usuarios de 80 años y más sobre total 65 y +. Hombres_Cantabria', 'Porcentaje usuarios de 80 años y más sobre total 65 y +. Hombres_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'porcen-usuarios-80-hombres.json-stat'},
        'porcen_usuarios_80_mujeres': {
            'sheet': 'Residencial',
            'category': 'Distribuciones por edad y sexo. Centros Residenciales',
            'label': 'Porcentaje usuarios de 80 años y más sobre total 65 y +. Mujeres',
            'variables': [],
            'rate_vars': ['Porcentaje usuarios de 80 años y más sobre total 65 y +. Mujeres_Cantabria', 'Porcentaje usuarios de 80 años y más sobre total 65 y +. Mujeres_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'porcen-usuarios-80-mujeres.json-stat'},
        'precio_publico_usuario': {
            'sheet': 'Residencial',
            'category': 'Precio público anual. Centros Residenciales',
            'label': 'Precio en euros por por año y usuario',
            'variables': [],
            'rate_vars': ['Precio público anual. Centros Residenciales_Precio en euros por por año y usuario_Cantabria', 'Precio público anual. Centros Residenciales_Precio en euros por por año y usuario_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'precio-publico-usuario.json-stat'},
        'precio_publico_aport_usuario': {
            'sheet': 'Residencial',
            'category': 'Precio público anual. Centros Residenciales',
            'label': 'Aportación promedio del usuario/a. €/año/Usuario',
            'variables': [],
            'rate_vars': ['Precio público anual. Centros Residenciales_Aportación promedio del usuario/a. €/año/Usuario_Cantabria', 'Precio público anual. Centros Residenciales_Aportación promedio del usuario/a. €/año/Usuario_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'precio-publico-aport-usuario.json-stat'},
        'precio_publico_aport_usuario_porcen': {
            'sheet': 'Residencial',
            'category': 'Precio público anual. Centros Residenciales',
            'label': 'Aportación promedio del usuario/a. Porcentaje sobre el precio',
            'variables': [],
            'rate_vars': ['Precio público anual. Centros Residenciales_Aportación promedio del usuario/a. Porcentaje sobre el precio_Cantabria', 'Precio público anual. Centros Residenciales_Aportación promedio del usuario/a. Porcentaje sobre el precio_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'precio-publico-aport-usuario-porcen.json-stat'},
        'precio_concentracion_usuario': {
            'sheet': 'Residencial',
            'category': 'Precio de concentración anual. Centros Residenciales',
            'label': 'Precio en euros por año y usuario',
            'variables': [],
            'rate_vars': ['Precio de concentración anual. Centros Residenciales_Precio en euros por año y usuario_Cantabria', 'Precio de concentración anual. Centros Residenciales_Precio en euros por año y usuario_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'precio-concentracion-usuario.json-stat'},
        'precio_concentracion_aport_usuario': {
            'sheet': 'Residencial',
            'category': 'Precio de concentración anual. Centros Residenciales',
            'label': 'Aportación promedio del usuario/a. €/año/Usuario',
            'variables': [],
            'rate_vars': ['Precio de concentración anual. Centros Residenciales_Aportación promedio del usuario/a. €/año/Usuario_Cantabria', 'Precio de concentración anual. Centros Residenciales_Aportación promedio del usuario/a. €/año/Usuario_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'precio-concentracion-aport-usuario.json-stat'},
        'precio_concentracion_aport_usuario_porcen': {
            'sheet': 'Residencial',
            'category': 'Precio de concentración anual. Centros Residenciales',
            'label': 'Aportación promedio del usuario/a. Porcentaje sobre el precio',
            'variables': [],
            'rate_vars': ['Precio de concentración anual. Centros Residenciales_Aportación promedio del usuario/a. Porcentaje sobre el precio_Cantabria', 'Precio de concentración anual. Centros Residenciales_Aportación promedio del usuario/a. Porcentaje sobre el precio_España'],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'}, 'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': 'precio-concentracion-aport-usuario-porcen.json-stat'}

    },
    'globals': {
        'csv': 'vision-global-residencias.csv'
    }
}

residences_cfg = Baseconfig(params)
residences_cfg.add(common_cfg)
