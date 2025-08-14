from flask_mail import Message
from app.infrastructure.email import mail  

def send_email(to: str, subject: str, body: str) -> None:
    msg = Message(subject=subject, recipients=[to], body=body)
    mail.send(msg)