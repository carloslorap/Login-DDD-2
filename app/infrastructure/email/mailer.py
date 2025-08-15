from flask_mail import Message
from app.infrastructure.email import mail  
import base64, re

def send_email(to: str, subject: str, body: str, image_data: str | None = None) -> None:
    msg = Message(subject=subject, recipients=[to], body=body)
    
       # Si viene una imagen como dataURL, la adjuntamos
    if image_data and image_data.startswith("data:"):
        header, b64 = image_data.split(",", 1)
        m = re.match(r"data:(.*?);base64", header)
        mime = m.group(1) if m else "application/octet-stream"
        ext = (mime.split("/")[-1] or "bin")
        data = base64.b64decode(b64)
        msg.attach(filename=f"adjunto.{ext}", content_type=mime, data=data)
    
    mail.send(msg)