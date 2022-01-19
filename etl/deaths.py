"""Deaths indicators."""

from etl.common import to_json_stat, write_to_file

from etl.config_deaths import deaths_cfg as cfg

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
        period1 = str(df.loc[i, 'Año'])
        period2 = '{:0>2}'.format(df.loc[i, 'Mes'])
        df.loc[i, 'period'] =  prefix + period1 + '-' + period2

    df.drop(columns={'Año', 'Mes'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Mes'}, inplace=True)
    df = df.tail(periods)
    df = df.round(2)
    return df

def replace_month(json_str):
    """Replace month number by its name."""
    json_str = json_str.replace('-01"', '-Ene"')
    json_str = json_str.replace('-02"', '-Feb"')
    json_str = json_str.replace('-03"', '-Mar"')
    json_str = json_str.replace('-04"', '-Abr"')
    json_str = json_str.replace('-05"', '-May"')
    json_str = json_str.replace('-06"', '-Jun"')
    json_str = json_str.replace('-07"', '-Jul"')
    json_str = json_str.replace('-08"', '-Ago"')
    json_str = json_str.replace('-09"', '-Sep"')
    json_str = json_str.replace('-10"', '-Oct"')
    json_str = json_str.replace('-11"', '-Nov"')
    json_str = json_str.replace('-12"', '-Dic"')
    return json_str

# Read  input files
data = xlsx(cfg.path.input)
print(cfg.path.input)
# print(data)
# Datasets
df_global = pd.DataFrame()
indicators = []
for key in cfg.series:
    print(key)
    variables = [
        'Año', 'Mes',
        cfg.series[key].variables[0]]
    if (len(cfg.series[key].variables) == 2):
        variables.append(cfg.series[key].variables[1])
    df = data[cfg.file]\
        [cfg.series[key].sheet][variables].copy()

    # Drop NA rows, if any
    df.dropna(axis=0, how='all', inplace=True)

    # Rename variables
    df.rename(
        columns={
            cfg.series[key].variables[0]: 'Cantabria',},
        inplace=True)
    if (len(cfg.series[key].variables) == 2):
        df.rename(
            columns={
                cfg.series[key].variables[1]: 'España',}, 
            inplace=True)

    # Remove .0 from Año and Mes
    df['Año'] = df['Año'].astype(str).replace('\.0', '', regex=True)
    df['Mes'] = df['Mes'].astype(str).replace('\.0', '', regex=True)

    # Merge global dataset
    df_cant = df[['Año', 'Mes', 'Cantabria']].copy()
    df_cant = transform(df_cant, cfg.periods.global_deaths, 'Cantabria - ')
    df_cant.set_index('Mes', inplace=True)
    df_cant = df_cant.transpose()
    df_cant.insert(0, 'Categoria', cfg.series[key].category)
    df_cant[' - Indicadores'] = cfg.series[key].label
    if (len(cfg.series[key].variables) == 2):
        df_esp = df[['Año', 'Mes', 'España']].copy()
        df_esp = transform(df_esp, cfg.periods.global_deaths, 'España - ')
        df_esp.set_index('Mes', inplace=True)
        df_esp = df_esp.transpose()
        df_esp[' - Indicadores'] = cfg.series[key].label
        df_cant = df_cant.merge(df_esp, on=' - Indicadores')

    indicators.append(df_cant)

    # Generate JSON-Stat dataset
    df = transform(df, cfg.periods.deaths)
    vars = ['Cantabria']
    if (len(cfg.series[key].variables) == 2):
        vars.append('España')
    json_file = to_json_stat(
        df,
        ['Mes'],
        vars,
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    json_file = replace_month(json_file)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json)

# Generate CSV global dataset
df_global = pd.concat(indicators, axis=0, verify_integrity=False)
df_global.to_csv(cfg.path.output + cfg.globals.csv, index=False)

print('\nEnd of process. Files generated successfully.')
