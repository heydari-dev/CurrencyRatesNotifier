import smtplib
from email.mime.text import MIMEText
from config import EMAIL_RECEIVER


def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['subject'] = subject
    msg['From'] = 'from@example.com'
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP('sandbox.smtp.mailtrap.io', 25) as mail_server:
        mail_server.login('048ce75671724e', 'daad3879bebeb7')
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
