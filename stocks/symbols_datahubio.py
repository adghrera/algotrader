# https://datahub.io/core/s-and-p-500-companies/r/constituents.json

from service.common_util import get_data_from_file


def load_stocks_from_file():
    data = get_data_from_file('symbols/constituents_json.json')
    print(data)
    # Name, Symbol, Sector
    return data
