ROLE_ADMIN = 1
ROLE_NORMAL = 2

def has_role(session, *roles) -> bool:
    """True si el usuario en sesión tiene alguno de los roles."""
    return session.get("tipo_usuario_id") in roles