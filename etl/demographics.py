"""Demographics indicators."""

from etl.common import to_json_stat, write_to_file

from etl.config_demographics import demographics_cfg as cfg

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
df_global = pd.DataFrame()
indicators = []
for key in cfg.series:

    variables = [
        'Año',
        cfg.series[key].variables[0], cfg.series[key].variables[1]]
    df = data[cfg.file]\
        [cfg.series[key].sheet][variables].copy()

    # Drop NA rows, if any
    df.dropna(axis=0, how='all', inplace=True)

    # Rename variables
    df.rename(
        columns={
            cfg.series[key].variables[0]: 'Cantabria',
            cfg.series[key].variables[1]: 'España'}, 
        inplace=True)

    # Remove .0 from Año
    df['Año'] = df['Año'].astype(str).replace('\.0', '', regex=True)

    # Merge global dataset
    df_cant = df[['Año', 'Cantabria']].copy()
    df_cant = transform(df_cant, cfg.periods.global_demographics, 'Cantabria - ')
    df_cant.set_index('Año', inplace=True)
    df_cant = df_cant.transpose()
    df_cant.insert(0, 'Categoria', cfg.series[key].category)
    df_cant[' - Indicadores'] = cfg.series[key].label
    df_esp = df[['Año', 'España']].copy()
    df_esp = transform(df_esp, cfg.periods.global_demographics, 'España - ')
    df_esp.set_index('Año', inplace=True)
    df_esp = df_esp.transpose()
    df_esp[' - Indicadores'] = cfg.series[key].label
    df_cant = df_cant.merge(df_esp, on=' - Indicadores')
    indicators.append(df_cant)

    # Generate JSON-Stat dataset
    df = transform(df, cfg.periods.demographics)
    json_file = to_json_stat(
        df,
        ['Año'],
        ['Cantabria', 'España'],
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json)

# Generate CSV global dataset
df_global = pd.concat(indicators, axis=0, verify_integrity=False)
df_global.to_csv(cfg.path.output + cfg.globals.csv, index=False)

print('\nEnd of process. Files generated successfully.')
