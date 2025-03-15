import requests
from config import url, rules
import json
from mail import send_smtp_email
from notification import send_sms
from datetime import datetime
from khayyam import JalaliDatetime


def get_rates():
    """
        Fetches exchange rates from data.fixer.io API.

        Returns:
            dict: JSON response containing exchange rates.
        """
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None  # Return None if request fails


def archive(filename, rates):
    """
        Creates a JSON archive of exchange rates.

        Args:
            filename (str): Name of the archive file.
            rates (dict): Exchange rates data to be saved.
        """
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))  # Save data in a readable JSON format


def send_mail(timestamp, rates):
    """
        Sends exchange rates via email.

        Args:
            timestamp (int): Timestamp of the rate data.
            rates (dict): Exchange rates to be sent.
        """
    now = JalaliDatetime(datetime.now()).strftime("%Y-%m-%d  %H:%M:%S")
    subject = f'{timestamp}-rates. dates: {now}'

    # Filter preferred currencies if specified in config
    if rules['email']['preferred'] is not None:
        tmp = dict()
        for exc in rules['email']['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp
    text = json.dumps(rates)

    send_smtp_email(subject, text)


def check_notify_rules(rates):
    """
       Checks exchange rates against user-defined notification rules.

       Args:
           rates (dict): Current exchange rates.

       Returns:
           str: Notification message if any rate exceeds limits; otherwise, an empty string.
       """
    msg = ''
    for exc in rules['notification']['preferred']:

        # Check if the rate is below the minimum threshold
        if rates[exc] <= rules['notification']['preferred'][exc]['min']:
            msg += f'{exc} less than your target min: {rates[exc]}\n'

        # Check if the rate is above the maximum threshold
        if rates[exc] >= rules['notification']['preferred'][exc]['max']:
            msg += f'{exc} bigger than your target max: {rates[exc]}\n'

    return msg


def send_notification(msg):
    """
       Sends an SMS notification if the message is not empty.

       Args:
           msg (str): The message to be sent.
       """
    now = JalaliDatetime(datetime.now()).strftime("%Y-%m-%d  %H:%M:%S")
    send_sms(f'date: {now}\n{msg}')


if __name__ == '__main__':
    data = get_rates()

    if data:  # Ensure data is not None before proceeding

        if rules['archive']:
            archive(data['timestamp'], data['rates'])

        if rules['email']['enable']:
            send_mail(data['timestamp'], data['rates'])

        if rules['notification']['enable']:
            notification_msg = check_notify_rules(data['rates'])

            if notification_msg:
                send_notification(notification_msg)

    else:
        print('Failed to fetch exchange rates.')

