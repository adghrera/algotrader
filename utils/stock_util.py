import os

from sqlalchemy import desc

from dbsetup import Symbol, db, Price
from stocks.stocks_tradier import get_historical_data
from stocks.symbols_datahubio import load_stocks_from_file
from compress_pickle import dump, load

def get_stock_prices(symbol):
    data = get_stock_prices_from_db(symbol)

    if not data:
        data = get_stock_prices_from_file(symbol)

    if not data:
        data = get_stock_prices_from_api(symbol)

    return data


def get_stock_prices_from_db(symbol):
    print(f'reading data from db {symbol}...')
    db_symbol = Symbol.query.filter(Symbol.symbol == symbol).first()
    if db_symbol:
        prices = Price.query.filter(Price.symbol_id == db_symbol.id).order_by(desc(Price.date)).all()
        if prices and prices.length > 0:
            return prices
    return None


def get_stock_prices_from_file(symbol):
    fp = os.path.join('/tmp/stock_data/historical', f'data_{symbol}.gz')
    if os.path.exists(fp):
        print(f'reading data from {fp}...')
        data = load(fp)
        print(data)
        return data
    else:
        print(f'file does not exist {fp}...')


def save_stock_prices_to_file(symbol, data):
    fp = os.path.join('/tmp/stock_data/historical', f'data_{symbol}.gz')
    if not os.path.exists(fp):
        dump(data, fp, compression="gzip")


def get_stock_prices_from_api(symbol):
    data = get_historical_data(symbol, start_date='2020-08-01')
    if data:
        print(f'Got prices data from api for {symbol}...')
        print(data)
        save_stock_prices_to_file(symbol, data)


def import_symbol_data():
    stocks = load_stocks_from_file()
    for stk in stocks:
        existing_symbol = Symbol.query.filter(Symbol.symbol == stk['Symbol']).first()
        # print(existing_symbol)

        if not existing_symbol:
            print(f'adding {stk["Symbol"]}...')
            symbol = Symbol(name=stk['Name'], symbol=stk['Symbol'], industry=stk['Sector'])
            db.session.add(symbol)
        else:
            print(f'found {stk["Symbol"]}...')

    print(f'Committing...')
    db.session.commit()
