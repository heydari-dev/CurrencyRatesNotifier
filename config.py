BASE_PATH = 'https://data.fixer.io/api/latest?access_key='
API_KEY = 'your apikey from site fixer.io'

url = BASE_PATH + API_KEY

rules = {
    'archive': True,
    'email': {
        'enable': False,
        'host_password': 'your password',
        'host': 'smtp.gmail.com',
        'host_user': 'your email',
        'port': 587,
        'port_ssl': 465,
        'receiver': 'email receiver',
        'preferred': ['USD', 'BTC', 'CAD', 'LRD']
    },
    'notification': {
        'enable': False,
        'api_key': 'your api key',
        'send_number': 'your number',
        'receiver': 'your receiver number',
        'preferred': {
            'USD': {'max': 1.092109, 'min': 1.080000},
            'BTC': {'max': 1.3384365e-05, 'min': 1.0000000e-05}
        }
    }
}
