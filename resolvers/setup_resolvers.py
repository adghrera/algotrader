from .hello_resolver import resolve_hello
from .info_resolver import resolve_info
from .prices_resolver import resolve_prices
from .symbols_resolver import resolve_symbols


def setup(query):
    query.set_field("hello", resolve_hello)
    query.set_field("info", resolve_info)
    query.set_field("symbols", resolve_symbols)
    query.set_field("prices", resolve_prices)

