from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import rules

EMAIL_HOST = rules['email']['host']
EMAIL_PORT_SSL = rules['email']['port_ssl']
EMAIL_HOST_USER = rules['email']['host_user']
EMAIL_HOST_PASSWORD = rules['email']['host_password']
EMAIL_RECEIVER = rules['email']['receiver']


def send_smtp_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.sendmail(EMAIL_HOST_USER, EMAIL_RECEIVER, msg.as_string())


