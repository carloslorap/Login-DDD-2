# app/infrastructure/repositories/respuesta_solicitud/respuesta_solicitud_repository_impl.py
from typing import List
from app.domain.solicitud.respuesta_solicitud import RespuestaSolicitud
from app.domain.solicitud.respuesta_solicitud_repository import RespuestaSolicitudRepository
from app.infrastructure.models.respuesta_solicitud_model import RespuestaSolicitudModel
from app.infrastructure.db.connection import SessionLocal

class RespuestaSolicitudRepositoryImpl(RespuestaSolicitudRepository):
    def listar_por_estado(self, estado_solicitud_id: int) -> List[RespuestaSolicitud]:
        with SessionLocal() as db:
            registros = (
                db.query(RespuestaSolicitudModel)
                .filter(RespuestaSolicitudModel.estado_solicitud_id == estado_solicitud_id)
                .all()
            )

            return [
                RespuestaSolicitud(
                    respuesta_solicitud_id=row.respuesta_solicitud_id,
                    nombre=row.nombre,
                    respuesta=row.respuesta,
                    estado_solicitud_id=row.estado_solicitud_id,
                    created_at=row.created_at,
                    updated_at=row.updated_at,
                    estado=row.estado
                )
                for row in registros
            ]
