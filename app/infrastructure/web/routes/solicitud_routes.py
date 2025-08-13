from flask import Blueprint, render_template,request,flash,redirect,url_for,session
from datetime import datetime
from app.infrastructure.repositories.solicitud.solicitud_repository_impl import SolicitudRepositoryImpl
from app.application.solicitud.solicitud_services import SolicitudService

# decoradores
from app.decorators.protection import login_required
from app.infrastructure.repositories.solicitud.respuesta_solicitud_repository_impl import (
    RespuestaSolicitudRepositoryImpl)
from app.application.solicitud.respuesta_solicitud_service import RespuestaSolicitudService

solicitudes_bp = Blueprint("solicitudes", __name__)

repo = SolicitudRepositoryImpl()
solicitud_service = SolicitudService(repo)

respuesta_repo = RespuestaSolicitudRepositoryImpl()
respuesta_service = RespuestaSolicitudService(respuesta_repo)


@solicitudes_bp.route("/solicitudes", methods=["GET"])
@login_required
def listar_solicitudes():
    
    nombre = request.args.get("nombre")
    fecha_inicio_str = request.args.get("fecha_inicio")
    fecha_fin_str = request.args.get("fecha_fin")

    fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d") if fecha_inicio_str else None
    fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d") if fecha_fin_str else None
    
    respuestas_aprobado = respuesta_service.listar_por_estado(2)


    solicitudes = solicitud_service.listar_filtrado(nombre, fecha_inicio, fecha_fin)
    return render_template("solicitudes.html", solicitudes=solicitudes,respuestas_aprobado=respuestas_aprobado)


@solicitudes_bp.route("/solicitudes/<int:solicitud_id>/aprobar", methods=["POST"])
@login_required
def aprobar(solicitud_id: int):
    usuario_actual = session.get("username")
    try:
        solicitud_service.aprobar(solicitud_id,usuario_actual)
        flash("Solicitud aprobada correctamente.", "success")
    except Exception as e:
        flash(f"Error al aprobar: {e}", "danger")
    return redirect(url_for("solicitudes.listar_solicitudes"))