BASE_PATH = 'https://data.fixer.io/api/latest?access_key='
API_KEY = 'e57bea001181aba9810477c2527c25ca'

url = BASE_PATH + API_KEY

EMAIL_RECEIVER = 'to@example.com'

rules = {
    'archive': True,
    'send_email': True,
    # preferred default is None
    # 'preferred': None
    'preferred': ['USD', 'BTC', 'CAD', 'LRD']
}
