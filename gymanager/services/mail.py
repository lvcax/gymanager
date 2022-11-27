from gymanager.extensions.mail_sender import mail
from flask import current_app, render_template
from flask_mail import Message

def send_mail(subject: str, to: list[str], template: str, **kwargs):
    """Makes the send email

    Args:
        subject (str): Email subject
        to (list[str]): Destination (could be more than one)
        template (str): The template used to format message
    """

    msg = Message(
        subject=subject,
        recipients=[to],
        sender=current_app.config.get("MAIL_SENDER")
    )

    msg.body = render_template(f"mails/{template}.txt", **kwargs)
    msg.html = render_template(f"mails/{template}.html", **kwargs)

    mail.send(msg)
