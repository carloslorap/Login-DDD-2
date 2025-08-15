# from flask_mail import Message
# from app.infrastructure.email import mail  
# import base64, re

# def send_email(to: str, subject: str, body: str, image_data: str | None = None) -> None:
#     msg = Message(subject=subject, recipients=[to], body=body)
#        # Si viene una imagen como dataURL, la adjuntamos
#     if image_data and image_data.startswith("data:"):
#         header, b64 = image_data.split(",", 1)
#         m = re.match(r"data:(.*?);base64", header)
#         mime = m.group(1) if m else "application/octet-stream"
#         ext = (mime.split("/")[-1] or "bin")
#         data = base64.b64decode(b64)
#         msg.attach(filename=f"adjunto.{ext}", content_type=mime, data=data)
    
#     mail.send(msg)


# app/infrastructure/email/mailer.py
from flask import render_template
from flask_mail import Message
from app.infrastructure.email import mail
import base64
import re


def _data_url_to_bytes(data_url: str):
    """
    Convierte 'data:image/png;base64,AAAA...' a (mime_type, raw_bytes).
    """
    m = re.match(r"^data:(?P<mime>[\w/-]+);base64,(?P<data>.+)$", data_url)
    if not m:
        raise ValueError("Formato de data URL inválido")
    mime = m.group("mime")
    raw = base64.b64decode(m.group("data"))
    return mime, raw


def send_templated_email(to: str,
                         subject: str,
                         *,
                         template_name: str = "email/SendAnswer.html",
                         context: dict = None,
                         image_data_url: str | None = None,
                         image_cid: str = "adj-1",
                         text_fallback: str | None = None):
    """
    Envía un email con plantilla HTML Jinja.
    - to: destinatario
    - subject: asunto
    - template_name: ruta de la plantilla Jinja
    - context: variables para la plantilla
    - image_data_url: dataURL 'data:image/...;base64,...' para adjunto inline (opcional)
    - image_cid: Content-ID para referenciar la imagen en el HTML (cid:...)
    - text_fallback: versión texto plano (opcional). Si no se pasa, se deriva del HTML básico.
    """
    context = context or {}
    html_ctx = dict(context)

    # Si hay imagen, pasamos el CID a la plantilla para <img src="cid:...">
    if image_data_url:
        html_ctx["imagen_cid"] = image_cid

    html_body = render_template(template_name, **html_ctx)

    # Texto plano de respaldo (muy básico)
    if not text_fallback:
        # quita tags muy por arriba (opcional mejorar)
        text_fallback = re.sub(r"<br\s*/?>", "\n", html_ctx.get("mensaje", ""))
        text_fallback = re.sub(r"<[^>]+>", "", text_fallback).strip() or " "

    msg = Message(subject=subject, recipients=[to], body=text_fallback)
    msg.html = html_body

    # Adjuntar imagen inline si viene dataURL
    if image_data_url:
        mime, raw = _data_url_to_bytes(image_data_url)
        # ejemplo: "image/png"
        ext = (mime.split("/")[-1] or "png").lower()
        filename = f"adjunto.{ext}"

        # Flask-Mail: usar disposition='inline' + Content-ID
        msg.attach(
            filename=filename,
            content_type=mime,
            data=raw,
            disposition='inline',
            headers={'Content-ID': f'<{image_cid}>'}
        )

    mail.send(msg)
