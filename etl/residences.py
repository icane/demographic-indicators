"""Residences indicators."""

from etl.common import to_json_stat, write_to_file

from etl.config_residences import residences_cfg as cfg

from etlstat.extractor.extractor import xlsx

import json

import pandas as pd


def transform(df, periods, prefix=''):
    """Slice dataframe. Generate time period column.
    
        df (dataframe): dataset
        periods (int): number of time periods
        prefix (str): prefix for time periods
    """
    for i in range(0, len(df)):
        period = str(df.loc[i, 'Año'])
        df.loc[i, 'period'] =  prefix + period

    df.drop(columns={'Año'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Año'}, inplace=True)
    df = df.tail(periods)
    df = df.round(2)
    return df


# Read  input files
data = xlsx(cfg.path.input)

# Datasets
# Centros, plazas y usuarios
variables = [
    'Año', 'Centros_Cantabria', 'Centros Residenciales_Cantabria',
    'Vivienda para mayores_Cantabria', 'Plazas_Cantabria',
    'Plazas_Centros Residenciales_Cantabria',
    'Plazas_Vivienda para mayores_Cantabria', 'Usuarios_Cantabria',
    'Centros_España', 'Centros Residenciales_España',
    'Vivienda para mayores_España', 'Plazas_España',
    'Plazas_Centros Residenciales_España',
    'Plazas_Vivienda para mayores_España', 'Usuarios_España']
df = data[cfg.file]\
        [cfg.tables.centros_plazas_usuarios.sheet][variables].copy()

# Drop NA rows, if any
df.dropna(axis=0, how='all', inplace=True)

# Rename columns
df.rename(
        columns={
            'Centros_Cantabria': 'Centros Cantabria',
            'Centros Residenciales_Cantabria': 'Centros Residenciales Cantabria',
            'Vivienda para mayores_Cantabria': 'Vivienda para mayores Cantabria',
            'Plazas_Cantabria': 'Plazas Cantabria',
            'Plazas_Centros Residenciales_Cantabria': 'Plazas Centros Residenciales Cantabria',
            'Plazas_Vivienda para mayores_Cantabria': 'Plazas Vivienda para mayores Cantabria',
            'Usuarios_Cantabria': 'Usuarios Cantabria',
            'Centros_España': 'Centros España',
            'Centros Residenciales_España': 'Centros Residenciales España',
            'Vivienda para mayores_España': 'Vivienda para mayores España',
            'Plazas_España': 'Plazas España',
            'Plazas_Centros Residenciales_España': 'Plazas Centros Residenciales España',
            'Plazas_Vivienda para mayores_España': 'Plazas Vivienda para mayores España',
            'Usuarios_España': 'Usuarios España'}, 
        inplace=True)

# Remove .0 from Año
df['Año'] = df['Año'].astype(str).replace('\.0', '', regex=True)

# Generate JSON-Stat dataset
df = transform(df, cfg.periods.residences)
variables = [
    'Centros Cantabria', 'Centros Residenciales Cantabria',
    'Vivienda para mayores Cantabria', 'Plazas Cantabria',
    'Plazas Centros Residenciales Cantabria',
    'Plazas Vivienda para mayores Cantabria', 'Usuarios Cantabria',
    'Centros España', 'Centros Residenciales España',
    'Vivienda para mayores España', 'Plazas España',
    'Plazas Centros Residenciales España',
    'Plazas Vivienda para mayores España', 'Usuarios España']
json_file = to_json_stat(
    df,
    ['Año'],
    variables,
    cfg.tables.centros_plazas_usuarios.source)
json_obj = json.loads(json_file)
json_obj['dimension']['Variables']['category']['unit'] = \
    cfg.tables.centros_plazas_usuarios.unit
json_obj['note'] = cfg.tables.centros_plazas_usuarios.note
json_file = json.dumps(json_obj)
write_to_file(json_file, cfg.path.output + \
    cfg.tables.centros_plazas_usuarios.json)

# global table
df_global = pd.DataFrame()
indicators = []
for key in cfg.series:

    variables = [
        'Año',
        cfg.series[key].rate_vars[0], cfg.series[key].rate_vars[1]]

    df = data[cfg.file]\
        [cfg.series[key].sheet][variables].copy()

    # Drop NA rows, if any
    df.dropna(axis=0, how='all', inplace=True)

    # Rename variables
    df.rename(
        columns={
            cfg.series[key].rate_vars[0]: 'Cantabria',
            cfg.series[key].rate_vars[1]: 'España'}, 
        inplace=True)

    # Remove .0 from Año
    df['Año'] = df['Año'].astype(str).replace('\.0', '', regex=True)

    # Merge global dataset
    df_cant = df[['Año', 'Cantabria']].copy()
    df_cant = transform(df_cant, cfg.periods.global_residences, 'Cantabria - ')
    df_cant.set_index('Año', inplace=True)
    df_cant = df_cant.transpose()
    df_cant.insert(0, 'Categoria', cfg.series[key].category)
    df_cant[' - Indicadores'] = cfg.series[key].label
    df_esp = df[['Año', 'España']].copy()
    df_esp = transform(df_esp, cfg.periods.global_residences, 'España - ')
    df_esp.set_index('Año', inplace=True)
    df_esp = df_esp.transpose()
    df_esp[' - Indicadores'] = cfg.series[key].label
    df_cant = df_cant.merge(df_esp, on=' - Indicadores')
    indicators.append(df_cant)

# Generate CSV global dataset
df_global = pd.concat(indicators, axis=0, verify_integrity=False)
df_global.to_csv(cfg.path.output + cfg.globals.csv, index=False)

print('\nEnd of process. Files generated successfully.')
