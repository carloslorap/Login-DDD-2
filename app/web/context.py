from flask import session
from app.core.roles import ROLE_ADMIN, ROLE_NORMAL, has_role as _has_role

def inject_role_helpers():
    """
    Variables disponibles en Jinja:
      - current_role
      - ROLE_ADMIN / ROLE_NORMAL
      - has_role(*roles)
    """
    def has_role(*roles):
        return _has_role(session, *roles)

    return {
        "current_role": session.get("tipo_usuario_id"),
        "ROLE_ADMIN": ROLE_ADMIN,
        "ROLE_NORMAL": ROLE_NORMAL,
        "has_role": has_role,
    }