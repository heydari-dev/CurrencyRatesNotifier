import requests
from config import url, rules
import json
from mail import send_smtp_email
from notification import send_sms
from datetime import datetime
from khayyam import JalaliDatetime


def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    now = JalaliDatetime(datetime.now()).strftime("%Y-%m-%d  %H:%M:%S")
    subject = f'{timestamp}-rates. dates: {now}'

    if rules['email']['preferred'] is not None:
        tmp = dict()
        for exc in rules['email']['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp
    text = json.dumps(rates)

    send_smtp_email(subject, text)


def check_notify_rules(rates):
    msg = ''
    for exc in rules['notification']['preferred']:
        if rates[exc] <= rules['notification']['preferred'][exc]['min']:
            msg += f'{exc} less than your target min: {rates[exc]}\n'

        if rates[exc] >= rules['notification']['preferred'][exc]['max']:
            msg += f'{exc} bigger than your target max: {rates[exc]}\n'

    return msg


def send_notification(msg):
    now = JalaliDatetime(datetime.now()).strftime("%Y-%m-%d  %H:%M:%S")
    send_sms(f'date: {now}\n{msg}')


if __name__ == '__main__':
    data = get_rates()

    if rules['archive']:
        archive(data['timestamp'], data['rates'])

    if rules['email']['enable']:
        send_mail(data['timestamp'], data['rates'])

    if rules['notification']['enable']:
        notification_msg = check_notify_rules(data['rates'])

        if notification_msg:
            send_notification(notification_msg)
