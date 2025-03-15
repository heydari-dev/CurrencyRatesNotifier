import ghasedak_sms
from config import rules

API_KEY = rules['notification']['api_key']
SENDER_NUMBER = rules['notification']['send_number']
RECEIVER_NUMBER = rules['notification']['receiver']


def send_sms(msg):
    sms_api = ghasedak_sms.Ghasedak(API_KEY)

    response = sms_api.send_single_sms(
        ghasedak_sms.SendSingleSmsInput(
            message=msg,
            receptor=RECEIVER_NUMBER,
            line_number=SENDER_NUMBER,
            send_date='',
            client_reference_id=''
        )
    )

    print(response)
