from ariadne import ScalarType


def get_scalars():
    date_scalar = ScalarType("Date", serializer=serialize_date, value_parser=parse_date_value, literal_parser=parse_date_literal)
    return [date_scalar]


def serialize_date(value):
    # return value.isoformat()
    return value


# @datetime_scalar.value_parser
def parse_date_value(value):
    # dateutil is provided by python-dateutil library
    if value:
        # return dateutil.parser.parse(value)
        return value


# @datetime_scalar.literal_parser
def parse_date_literal(ast):
    value = str(ast.value)
    return parse_date_value(value)  # reuse logic from parse_value