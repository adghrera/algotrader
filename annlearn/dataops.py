from utils.stock_util import get_stock_prices, import_symbol_data
import dbsetup


def do_import_symbols():
    import_symbol_data()


def do_get_data():
    get_stock_prices('AAPL')


if __name__ == '__main__':
    dbsetup.setup()
    do_get_data()