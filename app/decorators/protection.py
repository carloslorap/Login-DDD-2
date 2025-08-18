from functools import wraps
from flask import session, redirect, url_for, flash,abort


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("auth.login")) 
        return f(*args, **kwargs)
    return decorated_function

 
def isLoginReady(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is not None:
            flash("Ya iniciaste sesion.")
            return redirect(url_for("solicitudes.listar_solicitudes"))  
        return f(*args, **kwargs)
    return decorated_function



def roles_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user_role = session.get("tipo_usuario_id")
            if user_role is None:
                # no autenticado -> login_required ya se encargará en esa ruta
                abort(401)
            if user_role not in allowed_roles:
                # autenticado pero sin permiso -> 403, no redirigir
                abort(403)
            return f(*args, **kwargs)
        return wrapper
    return decorator