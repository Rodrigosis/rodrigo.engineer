from typing import List
from flask_mail import Mail, Message
import os


class TriggerEmail:

    def __init__(self, app):
        self.mail = Mail(app)

    def submit(self, issuer_name: str, message_body: str, sender: str, subject: str):
        message_body = sender + '\n\n' + message_body
        subject = issuer_name + ' - ' + subject

        msg = Message(subject, sender=os.environ.get('MAIL_USERNAME'), recipients=[os.environ.get('MAIL_DESTINATION')],
                      body=message_body)

        self.mail.send(msg)
