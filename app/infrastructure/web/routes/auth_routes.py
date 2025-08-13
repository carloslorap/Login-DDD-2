from flask import Blueprint, render_template, redirect, url_for, request, flash, session

# hasheo de contrasena
from app.infrastructure.auth.password_hasher import PasswordHasher

from app.infrastructure.repositories.auth.auth_repository_impl import AuthRepositoryImpl
from app.application.auth.login_user import LoginUser

# decoradores
from app.decorators.protection import login_required
from app.decorators.protection import isLoginReady

auth_bp = Blueprint("auth", __name__, template_folder="../templates")

# Instancias compartidas
auth_repository = AuthRepositoryImpl()
password_hasher = PasswordHasher()

login_use_case = LoginUser(auth_repository, password_hasher)

  

@auth_bp.route("/login", methods=["GET", "POST"])
@isLoginReady
def login():
    if request.method == "POST":
        username = request.form.get("username") 
        password = request.form.get("password")

        try:
            user = login_use_case.execute(username, password) 
            session["user_id"] = user.usuario_id
            session["username"] = user.usuario  
            return redirect(url_for("auth.dashboard"))
        except ValueError as e:
            flash(str(e))
 
    return render_template("login.html")


@auth_bp.route("/")
@login_required
def dashboard():
    return render_template("dashboard.html")

@auth_bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
