import smtplib
import ssl

from config import *


def send_mail(country):
    port = PORT
    smtp_server = SMTP_SERVER
    sender_email = SENDER_MAIL
    receiver_email = RECEIVER_MAIL
    password = SENDER_PASS
    message = TEXT.format(SUBJECT, country)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('Email sent...')
