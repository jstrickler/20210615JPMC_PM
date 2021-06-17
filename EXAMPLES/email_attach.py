#!/usr/bin/env python
import smtplib
from imghdr import what
from email.message import EmailMessage
from getpass import getpass


SMTP_SERVER = "smtp2go.com"  # <1>
SMTP_PORT = 2525

SMTP_USER = 'pythonclass'

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']


def main():
    smtp_server = create_smtp_server()
    msg = create_message(
        SENDER,
        RECIPIENTS,
        'Here is your attachment',
        'Testing email attachments from python class.\n\n',
    )
    add_text_attachment('../DATA/parrot.txt', msg)
    add_image_attachment('../DATA/felix_auto.jpeg', msg)
    send_message(smtp_server, msg)


def create_message(sender, recipients, subject, body):
    msg = EmailMessage()  # <2>
    msg.set_content(body)  # <3>
    msg['From'] = sender
    msg['To'] = recipients
    msg['Subject'] = subject
    return msg


def add_text_attachment(file_name, message):
    with open(file_name) as file_in:  # <4>
        attachment_data = file_in.read()
    message.add_attachment(attachment_data)  # <5>


def add_image_attachment(file_name, message):
    with open(file_name, 'rb') as file_in:  # <6>
        attachment_data = file_in.read()
    image_type = what(None, h=attachment_data)  # <7>
    message.add_attachment(attachment_data, maintype='image', subtype=image_type)  # <8>


def create_smtp_server():
    password = getpass("Enter SMTP server password:")  # <9>
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)  # <10>
    smtpserver.login(SMTP_USER, password)  # <11>

    return smtpserver


def send_message(server, message):
    try:
        server.send_message(message)  # <12>
    finally:
        server.quit()


if __name__ == '__main__':
    main()
