from flask import Blueprint, render_template, redirect, url_for, request, flash
import traceback

# hasheo de contrasena
from app.infrastructure.auth.password_hasher import PasswordHasher

# decoradores
from app.decorators.protection import login_required

from app.infrastructure.repositories.user.usuario_repository_impl import (
    TipoUsuarioRepositoryImpl,
    UserRepositoryImpl,
)
from app.application.user.user_services import TypeUserServices, UserServices


user_bp = Blueprint("user", import_name=__name__, template_folder="../templates")

# Instancias compartidas
password_hasher = PasswordHasher()
tipo_usuario_repository = TipoUsuarioRepositoryImpl()
user_repository = UserRepositoryImpl()

listar_tipos_usuario = TypeUserServices(tipo_usuario_repository)
user_services = UserServices(user_repository, password_hasher)


@user_bp.route("/user", methods=["GET", "POST"])
@login_required
def user_create():
    if request.method == "POST":
        nombres = request.form.get("nombres")
        ap_paterno = request.form.get("ap_paterno")
        ap_materno = request.form.get("ap_materno")
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")
        repetir_contrasena = request.form.get("repetir_contrasena")
        tipo_usuario_id = int(request.form.get("tipo_usuario"))

        # validacion de la contraseña
        if contrasena != repetir_contrasena:
            flash("Las contraseñas no coinciden", "danger")
            return redirect(url_for("user.user_create"))

        try:
            user_services.register_user(
                nombres=nombres,
                ap_paterno=ap_paterno,
                ap_materno=ap_materno,
                usuario=usuario,
                contrasena=contrasena,
                tipo_usuario_id=tipo_usuario_id,
            )

            flash("Usuario creado correctamente", "success")
            return redirect(url_for("auth.dashboard"))
        except Exception as e:
            traceback.print_exc()
            flash(f"Error al crear el usuario: {str(e)}", "danger")

    tipos_usuario = listar_tipos_usuario.execute()

    tipos_usuario = [
        {"id": item.tipo_usuario_id, "value": item.nombre} for item in tipos_usuario
    ]
    return render_template("user_create.html", tipos_usuario=tipos_usuario)


@user_bp.route("/change-password", methods=["POST","GET"])
def changePassword():
    return render_template("change_password.html")
