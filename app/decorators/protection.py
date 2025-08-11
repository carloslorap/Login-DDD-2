from functools import wraps
from flask import session, redirect, url_for, flash,request


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            flash("Debes iniciar sesión primero.")
            return redirect(url_for("auth.login")) 
        return f(*args, **kwargs)
    return decorated_function


def isLoginReady(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is not None:
            flash("Ya iniciaste sesion.")
            return redirect(url_for("auth.dashboard"))  
        return f(*args, **kwargs)
    return decorated_function

