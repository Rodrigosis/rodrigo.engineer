import os

from www.rodrigo.engineer import views


def create_site():
    app = views.app

    app.config.update(
        DEBUG=True,
        # EMAIL SETTINGS
        MAIL_SERVER=os.environ.get('MAIL_SERVER'),
        MAIL_PORT=os.environ.get('MAIL_PORT'),
        MAIL_USE_SSL=True,
        MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
        MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD'),
        MAIL_DESTINATION=os.environ.get('MAIL_DESTINATION')
    )

    return app
