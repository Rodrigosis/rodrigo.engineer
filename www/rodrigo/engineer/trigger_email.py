from flask_mail import Mail

from www.rodrigo.engineer.views import app


mail = Mail()
mail.init_app(app)


class TriggerEmail:

    def submit(self):
        pass
