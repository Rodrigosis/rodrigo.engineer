from typing import List
from flask_mail import Mail, Message


class TriggerEmail:

    def __init__(self, app):
        self.mail = Mail(app)

    def submit(self, subject: str, message_body: str, sender: str, recipients: List[str]):

        msg = Message(subject, sender=sender, recipients=recipients, body=message_body)
        # msg = Message(subject='teste',
        #               sender='rodrigo.sis.s6@gmail.com',
        #               recipients=['rodrigo.sis.s7@gmail.com'],
        #               body='test email')

        self.mail.send(msg)
