from math import ceil
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from app.infrastructure.email.mailer import send_templated_email
from datetime import datetime
from app.infrastructure.repositories.solicitud.solicitud_repository_impl import (
    SolicitudRepositoryImpl,
)
from app.application.solicitud.solicitud_services import SolicitudService

# decoradores
from app.decorators.protection import login_required, roles_required
from app.infrastructure.repositories.solicitud.respuesta_solicitud_repository_impl import (
    RespuestaSolicitudRepositoryImpl,
)
from app.application.solicitud.respuesta_solicitud_service import (
    RespuestaSolicitudService,
)
from app.core.roles import ROLE_ADMIN, ROLE_NORMAL

# from app.infrastructure.email.mailer import send_email
solicitudes_bp = Blueprint("solicitudes", __name__)

repo = SolicitudRepositoryImpl()
solicitud_service = SolicitudService(repo)

respuesta_repo = RespuestaSolicitudRepositoryImpl()
respuesta_service = RespuestaSolicitudService(respuesta_repo)




@solicitudes_bp.route("/solicitudes", methods=["GET"])
@login_required
@roles_required(ROLE_ADMIN,ROLE_NORMAL)
def listar_solicitudes():

    nombre = request.args.get("nombre")
    fecha_inicio_str = request.args.get("fecha_inicio")
    fecha_fin_str = request.args.get("fecha_fin")
    atendidos = request.args.get("atendidos")
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10)) 

    fecha_inicio = (
        datetime.strptime(fecha_inicio_str, "%Y-%m-%d") if fecha_inicio_str else None
    )
    fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d") if fecha_fin_str else None

    respuestas_aprobado = respuesta_service.listar_por_estado(2)
    respuesta_desaprobado = respuesta_service.listar_por_estado(3)


    solicitudes,total = solicitud_service.listar_filtrado(
        nombre, fecha_inicio, fecha_fin, atendidos, page, per_page
    )
    
    total_pages = ceil(total / per_page) if per_page else 1
    
    # Para construir URLs de paginación conservando filtros
    qs = request.args.to_dict(flat=True)

    qs.pop("page", None)
    qs.pop("per_page", None)
    
    return render_template(
        "solicitudes.html",
        solicitudes=solicitudes,
        respuestas_aprobado=respuestas_aprobado,
        respuesta_desaprobado=respuesta_desaprobado,
        # paginación
        page=page,
        per_page=per_page,
        total=total,
        total_pages=total_pages,
        qs=qs,
    )
    

@solicitudes_bp.route("/solicitudes/<int:solicitud_id>/aprobar", methods=["POST"])
@login_required
def aprobar(solicitud_id: int):
    usuario_actual = session.get("username")
    mensaje = request.form.get("mensaje", "").strip()
    destinatario = request.form.get("destinatario", "").strip()
    try:
        
        if destinatario and mensaje:
            send_templated_email(
                to=destinatario,
                subject="Respuesta a su solicitud",
                context={
                    "titulo": "¡Solicitud Aprobada!",
                    "nombre": request.form.get("nombre") or "",    # si lo tienes
                    "intro":  "Hemos revisado su solicitud y fue aprobada:",
                    "mensaje": mensaje,
                    "entidad": "Citas Médicas",
                    "soporte": "soporte@hospital.pe",
                },
                image_data_url=request.form.get("image_data") or None,  # si vino imagen desde el modal
                image_cid="adj-1"
            )
            solicitud_service.aprobar(solicitud_id, usuario_actual)
            flash("Solicitud aprobada y correo enviado.", "success")
        else:
            flash("debes enviar un mensaje","danger")
    except Exception as e:
        flash(f"Error al aprobar: {e}", "danger")
    return redirect(url_for("solicitudes.listar_solicitudes"))


@solicitudes_bp.route("/solicitudes/<int:solicitud_id>/desaprobar", methods=["POST"])
@login_required
def desaprobar(solicitud_id: int):
    usuario_actual = session.get("username")
    mensaje = request.form.get("mensaje", "").strip()
    destinatario = request.form.get("destinatario", "").strip()

    try:
        
        # 1) Envía email si hay destinatario y mensaje
        if destinatario and mensaje:
            send_templated_email(
                to=destinatario,
                subject="Respuesta a su solicitud",
                context={
                    "titulo": "¡Solicitud Desaprobada!",
                    "nombre": request.form.get("nombre") or "",    # si lo tienes
                    "intro":  "Hemos revisado su solicitud y fue desaprobada:",
                    "mensaje": mensaje,
                    "entidad": "Citas Médicas",
                    "soporte": "soporte@hospital.pe",
                },
                image_data_url=request.form.get("image_data") or None,  # si vino imagen desde el modal
                image_cid="adj-1"
            )
            # 2 ) Actualiza estado en BD
            solicitud_service.desaprobar(solicitud_id, usuario_actual)
            flash("Solicitud desaprobada y correo enviado.", "success")
        else:
            flash("debes enviar un mensaje","danger")
    except Exception as e:
        flash(f"Error al desaprobar/enviar correo: {e}", "danger")

    return redirect(url_for("solicitudes.listar_solicitudes"))
