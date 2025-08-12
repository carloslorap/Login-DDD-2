from flask import Blueprint, render_template,request
from datetime import datetime
from app.infrastructure.repositories.solicitud.solicitud_repository_impl import SolicitudRepositoryImpl
from app.application.solicitud.solicitud_services import SolicitudService

solicitudes_bp = Blueprint("solicitudes", __name__)

repo = SolicitudRepositoryImpl()
solicitud_service = SolicitudService(repo)


@solicitudes_bp.route("/solicitudes", methods=["GET"])
def listar_solicitudes():
    
    nombre = request.args.get("nombre")
    fecha_inicio_str = request.args.get("fecha_inicio")
    fecha_fin_str = request.args.get("fecha_fin")

    fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d") if fecha_inicio_str else None
    fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d") if fecha_fin_str else None

    
    solicitudes = solicitud_service.listar_filtrado(nombre, fecha_inicio, fecha_fin)
    return render_template("solicitudes.html", solicitudes=solicitudes)