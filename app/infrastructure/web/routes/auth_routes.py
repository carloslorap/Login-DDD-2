from flask import Blueprint, render_template, redirect, url_for, request, flash, session

# hasheo de contrasena
from app.infrastructure.auth.password_hasher import PasswordHasher

from app.infrastructure.repositories.auth.auth_repository_impl import AuthRepositoryImpl
from app.application.auth.login_user import LoginUser

from app.infrastructure.repositories.auth.auth_repository_impl import AuthRepositoryImpl


# decoradores
from app.decorators.protection import isLoginReady

auth_bp = Blueprint("auth", __name__, template_folder="../templates")

# Instancias compartidas
auth_repository = AuthRepositoryImpl()
password_hasher = PasswordHasher()

login_use_case = LoginUser(auth_repository, password_hasher)

  

@auth_bp.route("/login", methods=["GET", "POST"])
@isLoginReady
def login():
    errors = {}
    form = {"username": "", "contrasena": ""}

    if request.method == "POST":
        # leer y normalizar
        form["username"] = (request.form.get("username") or "").strip()
        form["contrasena"] = request.form.get("contrasena") or ""

        # validaciones
        if not form["username"]:
            errors["username"] = "El usuario es obligatorio."
        if not form["contrasena"]:
            errors["contrasena"] = "La contraseña es obligatoria."

        # solo intenta autenticar si no hay errores de formulario
        if not errors:
            try:
                user = login_use_case.execute(form["username"], form["contrasena"])
                session["user_id"] = user.usuario_id
                session["username"] = user.usuario
                session["tipo_usuario_id"] = user.tipo_usuario_id
                session["nombre_completo"] = user.full_name  
                flash("Bienvenido al Panel", "success")
                if session["tipo_usuario_id"] == 1:
                    return redirect(url_for("dashboard.dashboard"))
                else:
                 return redirect(url_for("solicitudes.listar_solicitudes"))
            except ValueError as e:
                flash(str(e), "error")

    # render con errores y valores actuales del form
    return render_template("login.html", errors=errors, form=form)


@auth_bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    flash("Sesión cerrada exitosamente","info")
    return redirect(url_for("auth.login"))




