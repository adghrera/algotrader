from stocks import stocks_tradier, symbols_datahubio


def resolve_hello(obj, info):
    # return stocks_tradier.get_quotes('SPY')
    return str(symbols_datahubio.load_stocks_from_file())