"""Test unitario del módulo residential.py."""

from beautifuldict.baseconfig import Baseconfig

from etlstat.extractor import extractor

from mock import patch

from pkg_resources import resource_filename

import pytest

from residencias.residential import Residential

import re

@pytest.fixture
def setup():
    """Configuración."""
    data_path = resource_filename('residencias', 'data/input/')

    common = {
        'path': {
            'input': data_path,
            'output': data_path
        },
        'config_col_name': 'Unnamed: 6',
        'encoding': 'utf-8',
        'data_extension': '*.[xX][lL][sS][xX]',
        'df_name': 'Residencias',
        'excel_name': 'Visión_general_DEMO.xlsx',
        'excel_data': 'Datos_carga_anuales_demo_final.xlsx',
        'sheet_data': 'Residencial',
        'separator': ';'
    }

    specific = {
        'single_dict': {
            'sheet': 'Residencial',
            'category': None,
            'label': None,
            'variables': [],
            'rate_vars': [],
            'source': 'Servicios Sociales dirigidos a Personas Mayores en España, Instituto de Mayores y Servicios Sociales (IMSERSO).',
            'unit': {
                'Cantabria': {
                    'decimals': 2, 'label': '%'},
                'España': {
                    'decimals': 2, 'label': '%'}},
            'note': [''],
            'json': None
        },
        'reglas': {
            'ñ': 'n',
            'á': 'a',
            'é': 'e',
            'í': 'i',
            'ó': 'o',
            'ú': 'u',
            '. ': '.',
            ' ': '-',
            '_': '-',
            '.': '-',
            '-del': '',
            '-de': '',
            ' a': '-',
            'por-': '',
            'en-': '',
            '-a-': '-',
            '-e-': '-',
            'y-': ''
        },
        'reglasEspecificas': {
            '-sobre-total-65-+': '',
            '-ano-mas': '',
            '-anos-mas': '',
            'usuario/a-€/ano/usuario': 'euro',
            'usuario/a-porcentaje-sobre-el-precio': 'porcentaje'
        }
    }
    resi_cfg = Baseconfig(common)
    resi_cfg.add(specific)
    return resi_cfg


# Obtengo la columna de las etiquetas y la transformo.
def test_download(setup):
    """Comprobar descarga del dataframe."""
    with patch.object(Residential, "__init__", lambda x, y: None):
        resi = Residential(None)
        resi.cfg = setup
        frame = extractor.xls(
            dir_path=resi.cfg.path.input,
            data_extension=resi.cfg.data_extension)
        resi.df = frame[resi.cfg.excel_name][resi.cfg.df_name]

        frame = extractor.xls(
            dir_path=resi.cfg.path.input,
            data_extension=resi.cfg.data_extension)
        resi.data = frame[resi.cfg.excel_data][resi.cfg.sheet_data]

        assert resi.df.shape == (39, 13)

        assert resi.data.shape == (7, 75)


def test_vars(setup):
    """Comprobar descarga del dataframe."""
    with patch.object(Residential, "__init__", lambda x, y: None):
        resi = Residential(None)
        resi.cfg = setup
        frame = extractor.xls(
            dir_path=resi.cfg.path.input,
            data_extension=resi.cfg.data_extension)
        resi.data = frame[resi.cfg.excel_data][resi.cfg.sheet_data]

    resi.transform_vars()

    assert len(resi.var_list) == (30)


def test_listLabels(setup):
    """Comprobar las columnas que sean category."""
    with patch.object(Residential, "__init__", lambda x, y: None):
        resi = Residential(None)
        resi.cfg = setup
        frame = extractor.xls(
            dir_path=resi.cfg.path.input,
            data_extension=resi.cfg.data_extension)
        resi.df = frame[resi.cfg.excel_name][resi.cfg.df_name]

        resi.listLabels()

        assert len(resi.labels) == 30


def test_name_json(setup):
    with patch.object(Residential, "__init__", lambda x, y: None):
        resi = Residential(None)
        resi.cfg = setup
        frame = extractor.xls(
            dir_path=resi.cfg.path.input,
            data_extension=resi.cfg.data_extension)
        resi.data = frame[resi.cfg.excel_data][resi.cfg.sheet_data]

    resi.json_vars = []

    resi.transform_vars()

    resi.name_json()

    assert len(resi.json_vars) == 30


def test_create_config(setup):
    """Comprobar las columnas que sean category."""
    with patch.object(Residential, "__init__", lambda x, y: None):
        resi = Residential(None)
        resi.cfg = setup
        frame = extractor.xls(
            dir_path=resi.cfg.path.input,
            data_extension=resi.cfg.data_extension)
        resi.df = frame[resi.cfg.excel_name][resi.cfg.df_name]

        frame = extractor.xls(
            dir_path=resi.cfg.path.input,
            data_extension=resi.cfg.data_extension)
        resi.data = frame[resi.cfg.excel_data][resi.cfg.sheet_data]

    resi.config_dict = {}

    resi.json_vars = []

    resi.single_dict = {
        'sheet': 'Residencial',
        'category': None,
        'label': None,
        'variables': [],
        'rate_vars': [],
        'source': None,
        'unit': {
            'Cantabria': {
                'decimals': 2, 'label': '%'},
            'España': {
                'decimals': 2, 'label': '%'}},
        'note': None,
        'json': None
    }

    resi.listLabels()

    resi.transform_vars()

    resi.name_json()

    resi.create_config()

    assert len(resi.config_dict) == 30

    print(resi.config_dict)


if __name__ == '__main__':
    pytest.main()
