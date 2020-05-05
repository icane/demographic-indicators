from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_mensual_demo.xlsx',
    'series': {
        'mortalidad': {
            'sheet': 'Defunciones meses',
            'label': 'Tasa de Mortalidad por 100.000 hab',
            'category': 'Tasas de mortalidad',
            'variables': [
                'TMortalidad_Cantabria',
                'TMortalidad_España'],
            'source': 'ICANE a partir de la explotación de la estadística de Defunciones del Movimiento Natural de Población, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': 'mortalidad.json-stat'
        },
        'mortalidad_hombres_total': {
            'sheet': 'Defunciones meses',
            'label': 'Tasa de mortalidad Hombres/población total por 100.000 hab',
            'category': 'Tasas de mortalidad',
            'variables': [
                'TMortalidad_Hombres_TOTAL_Cantabria',
                'TMortalidad_Hombres_TOTAL_España'],
            'source': 'ICANE a partir de la explotación de la estadística de Defunciones del Movimiento Natural de Población, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': 'mortalidad-hombres-total.json-stat'
        },
        'mortalidad_mujeres_total': {
            'sheet': 'Defunciones meses',
            'label': 'Tasa de mortalidad Mujeres/población total por 100.000 hab',
            'category': 'Tasas de mortalidad',
            'variables': [
                'TMortalidad_Mujeres_TOTAL_Cantabria',
                'TMortalidad_Mujeres_TOTAL_España'],
            'source': 'ICANE a partir de la explotación de la estadística de Defunciones del Movimiento Natural de Población, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': 'mortalidad-mujeres-total.json-stat'
        },
        'mortalidad_hombres': {
            'sheet': 'Defunciones meses',
            'label': 'Tasa de mortalidad Hombres por 100.000 hab',
            'category': 'Tasas de mortalidad',
            'variables': [
                'TMortalidad_Hombres_Cantabria',
                'TMortalidad_Hombres_España'],
            'source': 'ICANE a partir de la explotación de la estadística de Defunciones del Movimiento Natural de Población, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': 'mortalidad-hombres.json-stat'
        },
        'mortalidad_mujeres': {
            'sheet': 'Defunciones meses',
            'label': 'Tasa de mortalidad Mujeres por 100.000 hab',
            'category': 'Tasas de mortalidad',
            'variables': [
                'TMortalidad_Mujeres_Cantabria',
                'TMortalidad_Mujeres_España'],
            'source': 'ICANE a partir de la explotación de la estadística de Defunciones del Movimiento Natural de Población, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': 'mortalidad-mujeres.json-stat'
        },
        '001_008': {
            'sheet': 'Causas de muerte meses',
            'label': '001-008  I.Enfermedades infecciosas y parasitarias',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    001-008  I.Enfermedades infecciosas y parasitarias_Cantabria'],
                # 'TM_    001-008  I.Enfermedades infecciosas y parasitarias_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '001-008.json-stat'
        },
        '009_041': {
            'sheet': 'Causas de muerte meses',
            'label': '009-041  II.Tumores',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    009-041  II.Tumores_Cantabria'],
                # 'TM_    009-041  II.Tumores_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '009-041.json-stat'
        },
        '042_043': {
            'sheet': 'Causas de muerte meses',
            'label': '042-043  III.Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan al mecanismo de la inmunidad',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    042-043  III.Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan al mecanismo de la inmunidad_Cantabria'],
                # 'TM_    042-043  III.Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan al mecanismo de la inmunidad_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '042-043.json-stat'
        },
        '044_045': {
            'sheet': 'Causas de muerte meses',
            'label': '044-045  IV.Enfermedades endocrinas, nutricionales y metabólicas',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    044-045  IV.Enfermedades endocrinas, nutricionales y metabólicas_Cantabria'],
                # 'TM_    044-045  IV.Enfermedades endocrinas, nutricionales y metabólicas_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '044-045.json-stat'
        },
        '046_049': {
            'sheet': 'Causas de muerte meses',
            'label': '046-049  V.Trastornos mentales y del comportamiento',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    046-049  V.Trastornos mentales y del comportamiento_Cantabria'],
                # 'TM_    046-049  V.Trastornos mentales y del comportamiento_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '046-049.json-stat'
        },
        '050_052': {
            'sheet': 'Causas de muerte meses',
            'label': '050-052  VI-VIII.Enfermedades del sistema nervioso y de los órganos de los sentidos',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    050-052  VI-VIII.Enfermedades del sistema nervioso y de los órganos de los sentidos_Cantabria'],
                # 'TM_    050-052  VI-VIII.Enfermedades del sistema nervioso y de los órganos de los sentidos_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '050-052.json-stat'
        },
        '053_061': {
            'sheet': 'Causas de muerte meses',
            'label': '053-061 IX.Enfermedades del sistema circulatorio',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    053-061 IX.Enfermedades del sistema circulatorio_Cantabria'],
                # 'TM_    053-061 IX.Enfermedades del sistema circulatorio_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '053-061.json-stat'
        },
        '062_067': {
            'sheet': 'Causas de muerte meses',
            'label': '062-067  X.Enfermedades del sistema respiratorio',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    062-067  X.Enfermedades del sistema respiratorio_Cantabria'],
                # 'TM_    062-067  X.Enfermedades del sistema respiratorio_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '062-067.json-stat'
        },
        '068_072': {
            'sheet': 'Causas de muerte meses',
            'label': '068-072  XI.Enfermedades del sistema digestivo',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    068-072  XI.Enfermedades del sistema digestivo_Cantabria'],
                # 'TM_    068-072  XI.Enfermedades del sistema digestivo_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '068-072.json-stat'
        },
        '073': {
            'sheet': 'Causas de muerte meses',
            'label': '073  XII.Enfermedades de la piel y del tejido subcutáneo',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    073  XII.Enfermedades de la piel y del tejido subcutáneo_Cantabria'],
                # 'TM_    073  XII.Enfermedades de la piel y del tejido subcutáneo_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '073.json-stat'
        },
        '074_076': {
            'sheet': 'Causas de muerte meses',
            'label': '074-076  XIII.Enfermedades del sistema osteomuscular y del tejido conjuntivo',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    074-076  XIII.Enfermedades del sistema osteomuscular y del tejido conjuntivo_Cantabria'],
                # 'TM_    074-076  XIII.Enfermedades del sistema osteomuscular y del tejido conjuntivo_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '074-076.json-stat'
        },
        '077_080': {
            'sheet': 'Causas de muerte meses',
            'label': '077-080  XIV.Enfermedades del sistema genitourinario',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    077-080  XIV.Enfermedades del sistema genitourinario_Cantabria'],
                # 'TM_    077-080  XIV.Enfermedades del sistema genitourinario_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '077-080.json-stat'
        },
        '081': {
            'sheet': 'Causas de muerte meses',
            'label': '081  XV.Embarazo, parto y puerperio',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    081  XV.Embarazo, parto y puerperio_Cantabria'],
                # 'TM_    081  XV.Embarazo, parto y puerperio_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '081.json-stat'
        },
        '082': {
            'sheet': 'Causas de muerte meses',
            'label': '082  XVI.Afecciones originadas en el periodo perinatal',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    082  XVI.Afecciones originadas en el periodo perinatal_Cantabria'],
                # 'TM_    082  XVI.Afecciones originadas en el periodo perinatal_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '082.json-stat'
        },
        '083_085': {
            'sheet': 'Causas de muerte meses',
            'label': '083-085  XVII.Malformaciones congénitas, deformidades y anomalías cromosómicas',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    083-085  XVII.Malformaciones congénitas, deformidades y anomalías cromosómicas_Cantabria'],
                # 'TM_    083-085  XVII.Malformaciones congénitas, deformidades y anomalías cromosómicas_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '083-085.json-stat'
        },
        '086_089': {
            'sheet': 'Causas de muerte meses',
            'label': '086-089  XVIII.Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    086-089  XVIII.Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte_Cantabria'],
                # 'TM_    086-089  XVIII.Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '086-089.json-stat'
        },
        '090_102': {
            'sheet': 'Causas de muerte meses',
            'label': '090-102  XX.Causas externas de mortalidad',
            'category': 'Defunciones por causa de muerte. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    090-102  XX.Causas externas de mortalidad_Cantabria'],
                # 'TM_    090-102  XX.Causas externas de mortalidad_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '090-102.json-stat'
        },
        '062': {
            'sheet': 'Causas_muerte_respiratorias',
            'label': '062  Influenza (gripe) (incluye gripe aviar y gripe A)',
            'category': 'Defunciones causas 062-067  X.Enfermedades del sistema respiratorio. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    062  Influenza (gripe) (incluye gripe aviar y gripe A)_Cantabria'],
                # 'TM_    062  Influenza (gripe) (incluye gripe aviar y gripe A)_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '062.json-stat'
        },
        '063': {
            'sheet': 'Causas_muerte_respiratorias',
            'label': '063  Neumonía',
            'category': 'Defunciones causas 062-067  X.Enfermedades del sistema respiratorio. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    063  Neumonía_Cantabria'],
                # 'TM_    063  Neumonía_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '063.json-stat'
        },
        '064': {
            'sheet': 'Causas_muerte_respiratorias',
            'label': '064  Enfermedades crónicas de las vías respiratorias inferiores (excepto asma)',
            'category': 'Defunciones causas 062-067  X.Enfermedades del sistema respiratorio. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    064  Enfermedades crónicas de las vías respiratorias inferiores (excepto asma)_Cantabria'],
                # 'TM_    064  Enfermedades crónicas de las vías respiratorias inferiores (excepto asma)_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '064.json-stat'
        },
        '065': {
            'sheet': 'Causas_muerte_respiratorias',
            'label': '065  Asma',
            'category': 'Defunciones causas 062-067  X.Enfermedades del sistema respiratorio. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    065  Asma_Cantabria'],
                # 'TM_    065  Asma_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '065.json-stat'
        },
        '066': {
            'sheet': 'Causas_muerte_respiratorias',
            'label': '066  Insuficiencia respiratoria',
            'category': 'Defunciones causas 062-067  X.Enfermedades del sistema respiratorio. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    066  Insuficiencia respiratoria_Cantabria'],
                # 'TM_    066  Insuficiencia respiratoria_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '066.json-stat'
        },
        '067': {
            'sheet': 'Causas_muerte_respiratorias',
            'label': '067  Otras enfermedades del sistema respiratorio',
            'category': 'Defunciones causas 062-067  X.Enfermedades del sistema respiratorio. Tasas de defunciones por 100.000 habitantes',
            'variables': [
                'TM_    067  Otras enfermedades del sistema respiratorio_Cantabria'],
                # 'TM_    067  Otras enfermedades del sistema respiratorio_España'],
            'source': 'ICANE a partir de la explotación de microdatos de Defunciones por causa de muerte, INE',
            'unit':{
                'Cantabria': {'decimals': 0, 'label': 'Tanto por cienmil'},
                # 'España': {'decimals': 0, 'label': 'Tanto por cienmil'}
            },
            'note': ['Los datos de 2019 son provisionales'],
            'json': '067.json-stat'
        }
    },
    'globals': {
        'csv': 'vision-global-defunciones.csv'
    }
}

deaths_cfg = Baseconfig(params)
deaths_cfg.add(common_cfg)
