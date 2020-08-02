import requests

token = 'qHzSmYOrqPa200TO1o9FkIA6ubqu'
tradierUrl = 'https://sandbox.tradier.com'


def get_quotes(symbol):
    # Request: Market Quotes (https://sandbox.tradier.com/v1/markets/quotes?symbols=spy)

    # connection = httplib.HTTPSConnection('sandbox.tradier.com', 443, timeout = 30)

    # Headers

    headers = {"Accept":"application/json",
               "Authorization": f'Bearer {token}'}

    url = f'{tradierUrl}/v1/markets/quotes?symbols={symbol}'
    r = requests.get(url, headers=headers)
    print(r.json())
    return str(r.json())

    # Send synchronously
    #
    # connection.request('GET', '/v1/markets/quotes?symbols=spy', None, headers)
    # try:
    #   response = connection.getresponse()
    #   content = response.read()
    #   # Success
    #   print('Response status ' + str(response.status))
    # except httplib.HTTPException as e:
    #   # Exception
    #   print('Exception during request')