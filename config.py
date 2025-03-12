BASE_PATH = 'https://data.fixer.io/api/latest?access_key='
API_KEY = 'e57bea001181aba9810477c2527c25ca'

url = BASE_PATH + API_KEY

rules = {
    'archive': True,
    'email': {
        'enable': True,
        'receiver': 'to@example.com',
        'preferred': ['USD', 'BTC', 'CAD', 'LRD']
    },
    'notification': {
        'enable': True,
        'receiver': '059531',
        'preferred': {
            'USD': {'max': 1.092109, 'min': 1.080000},
            'BTC': {'max': 1.3384365e-05, 'min': 1.0000000e-05}
        }
    }
}
