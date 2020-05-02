"""Maps datasets."""

from etl.common import to_json_stat, write_to_file

from etl.config_maps import maps_cfg as cfg

from etlstat.extractor.extractor import xlsx

import json

import pandas as pd


# Read  input files
data = xlsx(cfg.path.input)

# Datasets
for key in cfg.series:
    df = data[cfg.file][cfg.series[key].sheet][
        cfg.series[key].variables].copy()

    # Drop NA rows, if any
    df.dropna(axis=0, how='all', inplace=True)

    # Rename variables
    df.rename(
        columns={
            cfg.series[key].variables[1]: cfg.series[key].label}, 
        inplace=True)

    # Remove .0 from COD_INE
    df['COD_INE'] = df['COD_INE'].astype(str).replace('\.0', '', regex=True)

    # Generate JSON-Stat dataset
    json_file = to_json_stat(
        df,
        ['COD_INE'],
        [cfg.series[key].label],
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json)

print('\nEnd of process. Files generated successfully.')