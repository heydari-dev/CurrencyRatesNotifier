import requests
from config import url
import json

def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None

def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


if __name__ == '__main__':
    data = get_rates()
    archive(data['timestamp'], data['rates'])