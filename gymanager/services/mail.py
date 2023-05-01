from flask import current_app, render_template
from flask_mail import Message

from gymanager.extensions.mailer import mail


def send_mail(subject, to, template, **kwargs):
    msg = Message(
        subject=subject,
        recipients=[to],
        sender=current_app.config["MAIL_SENDER"]
    )

    msg.body = render_template(f"mails/{template}.txt", **kwargs)
    msg.html = render_template(f"mails/{template}.html", **kwargs)

    mail.send(msg)
