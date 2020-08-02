import json
import os
from service.consts import DATA_PATH


def get_data_from_file(fpath):
    fp = os.path.join(DATA_PATH, fpath)
    if os.path.exists(fp):
        with open(fp) as p:
            return json.load(p)


def save_data(fpath, json_data):
    fp = os.path.join(DATA_PATH, fpath)
    with open(fp, 'w') as p:
        json.dump(json_data, p)
