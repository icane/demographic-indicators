"""Deaths indicators."""

from etl.common import to_json_stat, write_to_file

from etl.config_deaths_virus import deaths_cfg as cfg

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
    variables = ['Mes']
    variables.extend(cfg.series[key].variables)
    df = data[cfg.file][cfg.series[key].sheet][variables].copy()
    df.dropna(axis=0, how='all', inplace=True)
    df = df.round(2)
    json_file = to_json_stat(
        df,
        ['Mes'],
        cfg.series[key].variables,
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    print(key)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json)

# Generate CSV global dataset
# df_global = pd.concat(indicators, axis=0, verify_integrity=False)
# print(df_global)
# df_global.to_csv(cfg.path.output + cfg.globals.csv, index=False)

print('\nEnd of process. Files generated successfully.')
