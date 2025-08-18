from flask import Blueprint, render_template, redirect, url_for, request, flash,session
import traceback

# hasheo de contrasena
from app.infrastructure.auth.password_hasher import PasswordHasher

# decoradores
from app.decorators.protection import login_required, roles_required

from app.infrastructure.repositories.user.usuario_repository_impl import (
    TipoUsuarioRepositoryImpl,
    UserRepositoryImpl,
)
from app.application.user.user_services import TypeUserServices, UserServices
from app.core.roles import ROLE_ADMIN, ROLE_NORMAL


user_bp = Blueprint("user", import_name=__name__, template_folder="../templates")

# Instancias compartidas
password_hasher = PasswordHasher()
tipo_usuario_repository = TipoUsuarioRepositoryImpl()
user_repository = UserRepositoryImpl()

listar_tipos_usuario = TypeUserServices(tipo_usuario_repository)
user_services = UserServices(user_repository, password_hasher)


@user_bp.route("/user", methods=["GET", "POST"])
@login_required
@roles_required(ROLE_ADMIN)
def user_create():
    errors = {}
    # valores por defecto para repoblar el form
    form = {
        "nombres": "",
        "ap_paterno": "",
        "ap_materno": "",
        "usuario": "",
        "tipo_usuario": "",
    }

    if request.method == "POST":
        # leer
        form["nombres"] = (request.form.get("nombres") or "").strip()
        form["ap_paterno"] = (request.form.get("ap_paterno") or "").strip()
        form["ap_materno"] = (request.form.get("ap_materno") or "").strip()
        form["usuario"] = (request.form.get("usuario") or "").strip()
        form["tipo_usuario"] = (request.form.get("tipo_usuario") or "").strip()

        contrasena = request.form.get("contrasena") or ""
        repetir_contrasena = request.form.get("repetir_contrasena") or ""

        # validaciones requeridos
        if not form["nombres"]:
            errors["nombres"] = "Los nombres son obligatorios."
        if not form["ap_paterno"]:
            errors["ap_paterno"] = "El apellido paterno es obligatorio."
        if not form["ap_materno"]:
            errors["ap_materno"] = "El apellido materno es obligatorio."
        if not form["usuario"]:
            errors["usuario"] = "El usuario es obligatorio."
        if not form["tipo_usuario"]:
            errors["tipo_usuario"] = "Selecciona un tipo de usuario."

        # validaciones de contraseña
        if not contrasena:
            errors["contrasena"] = "La contraseña es obligatoria."
        elif len(contrasena) < 6:
            errors["contrasena"] = "Mínimo 6 caracteres."
        if repetir_contrasena != contrasena:
            flash("Las contraseñas no coinciden.","danger")
            errors["repetir_contrasena"] = ""

        # intenta registrar solo si no hay errores
        if not errors:
            try:
                tipo_usuario_id = int(form["tipo_usuario"])
            except (TypeError, ValueError):
                errors["tipo_usuario"] = "Tipo de usuario inválido."
            else:
                try:
                    user_services.register_user(
                        nombres=form["nombres"],
                        ap_paterno=form["ap_paterno"],
                        ap_materno=form["ap_materno"],
                        usuario=form["usuario"],
                        contrasena=contrasena,
                        tipo_usuario_id=tipo_usuario_id,
                    )
                    flash("Usuario creado correctamente", "success")
                    return redirect(url_for("user.user_create"))
                except ValueError as ve:
                    # ej: usuario ya existe u otra regla de dominio
                    errors["usuario"] = str(ve)
                except Exception as e:
                    traceback.print_exc()
                    flash(f"Error al crear el usuario: {str(e)}", "danger")

    # cargar tipos de usuario para el selector
    tipos_usuario = listar_tipos_usuario.execute()
    tipos_usuario = [{"id": t.tipo_usuario_id, "value": t.nombre} for t in tipos_usuario]

    return render_template(
        "user_create.html",
        tipos_usuario=tipos_usuario,
        errors=errors,
        form=form,
    )



@user_bp.route("/change-password", methods=["GET", "POST"])
@login_required
@roles_required(ROLE_ADMIN, ROLE_NORMAL)  # ambos roles pueden cambiar su pass
def change_password():
    errors = {}
    if request.method == "POST":
        current_password = (request.form.get("current_password") or "").strip()
        new_password = (request.form.get("new_password") or "").strip()
        confirm_password = (request.form.get("confirm_password") or "").strip()

        # Validaciones simples
        if not current_password:
            errors["current_password"] = "Ingresa tu contraseña actual."
        if not new_password:
            errors["new_password"] = "Ingresa la nueva contraseña."
        elif len(new_password) < 6:
            flash("La nueva contraseña debe tener al menos 6 caracteres.","danger")
            errors["new_password"] = ""
        if confirm_password != new_password:
            flash("La confirmación no coincide.","danger")
            errors["confirm_password"] = ""

        if not errors:
            try:
                user_id = session.get("user_id")
                if not user_id:
                    flash("Sesión no válida. Inicia sesión nuevamente.", "danger")
                    return redirect(url_for("auth.login"))

                user_services.change_password(user_id, current_password, new_password)
                flash("Contraseña actualizada correctamente.", "success")
                return redirect(url_for("user.change_password"))
            except ValueError as ve:
                # Errores de negocio: contraseña actual incorrecta, etc.
                flash(str(ve), "danger")
            except Exception as e:
                traceback.print_exc()
                flash("Ocurrió un error al actualizar la contraseña.", "danger")

    # GET o si hubo errores, renderizar el formulario
    return render_template("change_password.html", errors=errors)

