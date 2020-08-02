from stocks import stocks_tradier


def resolve_info(obj, info, symbol):
    return stocks_tradier.get_quotes(symbol)