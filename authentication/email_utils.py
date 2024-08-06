from flask import render_template
from flask_mail import Mail, Message
from .app import app

mail = Mail(app)


def send_email(to, subject, template, **kwargs):
    msg = Message(
        subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
