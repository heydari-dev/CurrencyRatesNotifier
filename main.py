import requests
from config import url, rules
import json
from mail import send_smtp_email


def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_email(timestamp, rates):
    subject = f'{timestamp} rates'
    tmp = dict()
    if rules['preferred'] is not None:
        for exc in rules['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp
    text = json.dumps(rates)

    send_smtp_email(subject, text)


if __name__ == '__main__':
    data = get_rates()

    if rules['archive']:
        archive(data['timestamp'], data['rates'])

    if rules['send_email']:
        send_email(data['timestamp'], data['rates'])
