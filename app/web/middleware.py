from flask import g, session
from itsdangerous import BadSignature, BadTimeSignature

def register_session_sanitizer(app):
    @app.before_request
    def _try_load_session():
        """Si la cookie de sesión está corrupta, limpia la sesión SIN redirigir."""
        try:
            _ = session.get("user_id", None)  # fuerza verificación
        except (BadSignature, BadTimeSignature):
            g._bad_session = True
            session.clear()

    @app.after_request
    def _maybe_drop_session_cookie(resp):
        """Si detectamos cookie mala, borramos la cookie en la respuesta actual."""
        if getattr(g, "_bad_session", False):
            resp.delete_cookie(app.config.get("SESSION_COOKIE_NAME", "session"))
        return resp