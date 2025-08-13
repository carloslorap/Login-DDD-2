# app/application/respuesta_solicitud/respuesta_solicitud_service.py
from typing import List
from app.domain.solicitud.respuesta_solicitud import RespuestaSolicitud
from app.domain.solicitud.respuesta_solicitud_repository import RespuestaSolicitudRepository

class RespuestaSolicitudService:
    def __init__(self, repository: RespuestaSolicitudRepository):
        self.repository = repository

    def listar_por_estado(self, estado_solicitud_id: int) -> List[RespuestaSolicitud]:
        return self.repository.listar_por_estado(estado_solicitud_id)
