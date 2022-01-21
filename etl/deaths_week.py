"""Deaths indicators."""

from etl.common import to_json_stat, write_to_file

from etl.config_deaths_week import deaths_week_cfg as cfg

from etlstat.extractor.extractor import xlsx

import json

import pandas as pd


def transform(df, periods, prefix=''):
    """Slice dataframe.
    
        df (dataframe): dataset
        periods (int): number of time periods
        prefix (str): prefix for time periods
    """
    for i in range(0, len(df)):
        period1 = str(df.loc[i, 'Semana'])
        df.loc[i, 'period'] =  prefix + period1

    df.drop(columns={'Semana'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Semana'}, inplace=True)
    df = df.tail(periods)
    df = df.round(2)
    return df

# Read  input files
data = xlsx(cfg.path.input)

# Global dataset
df_global = pd.DataFrame()
indicators = []
for key in cfg.series:
    variables = [
        'Semana',
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
            cfg.series[key].variables[0]: 'Cantabria'},
        inplace=True)
    if (len(cfg.series[key].variables) == 2):
        df.rename(
            columns={
                cfg.series[key].variables[1]: 'España'}, 
            inplace=True)

    # Merge global dataset
    df_cant = df[['Semana', 'Cantabria']].copy()
    df_cant = transform(df_cant, cfg.periods.global_deaths, 'Cantabria - ')
    df_cant.set_index('Semana', inplace=True)
    df_cant = df_cant.transpose()
    df_cant.insert(0, 'Categoria', cfg.series[key].category)
    df_cant[' - Indicadores'] = cfg.series[key].label
    if (len(cfg.series[key].variables) == 2):
        df_esp = df[['Semana', 'España']].copy()
        df_esp = transform(df_esp, cfg.periods.global_deaths, 'España - ')
        df_esp.set_index('Semana', inplace=True)
        df_esp = df_esp.transpose()
        df_esp[' - Indicadores'] = cfg.series[key].label
        df_cant = df_cant.merge(df_esp, on=' - Indicadores')

    indicators.append(df_cant)

    # Generate JSON-Stat dataset
    '''
    df = transform(df, cfg.periods.deaths)
    vars = ['Cantabria']
    if (len(cfg.series[key].variables) == 2):
        vars.append('España')
    json_file = to_json_stat(
        df,
        ['Semana'],
        vars,
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json)
    '''
# Generate CSV global dataset
df_global = pd.concat(indicators, axis=0, verify_integrity=False)
df_global.to_csv(cfg.path.output + cfg.globals.csv, index=False)

# Widgets
for key in cfg.widgets:
    variables = ['Semana']
    variables.extend(cfg.widgets[key].variables)
    print(variables)
    df = data[cfg.file][cfg.widgets[key].sheet][variables].copy()
    df.dropna(axis=0, how='all', inplace=True)
    df = df.round(2)
    json_file = to_json_stat(
        df,
        ['Semana'],
        cfg.widgets[key].variables,
        cfg.widgets[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.widgets[key].unit
    json_obj['note'] = cfg.widgets[key].note
    json_file = json.dumps(json_obj)
    print(key)
    write_to_file(json_file, cfg.path.output + cfg.widgets[key].json)

# Graphs
for key in cfg.graphs:
    variables = ['Semana']
    variables.extend(cfg.graphs[key].variables)
    print(variables)
    df = data[cfg.file][cfg.graphs[key].sheet][variables].copy()
    df.dropna(axis=0, how='all', inplace=True)
    df = df.round(2)
    json_file = to_json_stat(
        df,
        ['Semana'],
        cfg.graphs[key].variables,
        cfg.graphs[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.graphs[key].unit
    json_obj['note'] = cfg.graphs[key].note
    json_file = json.dumps(json_obj)
    print(key)
    write_to_file(json_file, cfg.path.output + cfg.graphs[key].json)


print('\nEnd of process. Files generated successfully.')
