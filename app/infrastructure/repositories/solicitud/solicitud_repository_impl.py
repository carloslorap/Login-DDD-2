from typing import List,Optional
from app.domain.solicitud.solicitud import Solicitud
from datetime import datetime
from app.domain.solicitud.solicitud_repository import SolicitudRepository
from app.infrastructure.models.solicitud_model import SolicitudModel
from app.infrastructure.db.connection import SessionLocal
from app.infrastructure.models.especialidad_model import EspecialidadModel

class SolicitudRepositoryImpl(SolicitudRepository):

    def listar_filtrado(
        self,
        nombre: Optional[str] = None,
        fecha_inicio: Optional[datetime] = None,
        fecha_fin: Optional[datetime] = None
    ) -> List[Solicitud]:
        with SessionLocal() as db:
            query = (
                db.query(SolicitudModel, EspecialidadModel.nombre.label("especialidad_nombre"))
                .join(EspecialidadModel, SolicitudModel.especialidad_id == EspecialidadModel.especialidad_id)
                .filter(SolicitudModel.estado == True, SolicitudModel.atendido == 0)
            )

            if nombre:
                query = query.filter(SolicitudModel.nombres.ilike(f"%{nombre}%"))

            if fecha_inicio and fecha_fin:
                query = query.filter(SolicitudModel.created_at.between(fecha_inicio, fecha_fin))

            registros = query.all()

            return [
                Solicitud(
                    solicitud_id=row.SolicitudModel.solicitud_id,
                    jid_id=row.SolicitudModel.jid_id,
                    especialidad_id=row.SolicitudModel.especialidad_id,
                    especialidad_nombre=row.especialidad_nombre,
                    nombres=row.SolicitudModel.nombres,
                    tipo_documento_id=row.SolicitudModel.tipo_documento_id,
                    numero_documento=row.SolicitudModel.numero_documento,
                    telefono=row.SolicitudModel.telefono,
                    email=row.SolicitudModel.email,
                    continuador=row.SolicitudModel.continuador,
                    sis=row.SolicitudModel.sis,
                    atendido=row.SolicitudModel.atendido,
                    estado=row.SolicitudModel.estado,
                    estado_solicitud_id=row.SolicitudModel.estado_solicitud_id,
                    usuario=row.SolicitudModel.usuario,
                    interconsulta=row.SolicitudModel.interconsulta,
                    interconsulta_imagen=row.SolicitudModel.interconsulta_imagen,
                    created_at=row.SolicitudModel.created_at,
                    updated_at=row.SolicitudModel.updated_at
                )
                for row in registros
            ]       

    def actualizar_estado_y_atendido(
        self,
        solicitud_id: int,
        nuevo_estado_id: int,
        atendido: int,
        usuario:str
    ) -> None:
        with SessionLocal() as db:
            try:
                filas = (
                    db.query(SolicitudModel)
                    .filter(SolicitudModel.solicitud_id == int(solicitud_id))
                    .update({
                        SolicitudModel.estado_solicitud_id: int(nuevo_estado_id),
                        SolicitudModel.atendido: int(atendido),
                        SolicitudModel.usuario: usuario, 
                        SolicitudModel.updated_at: datetime.now(),
                    }, synchronize_session=False)
                )
                db.commit()
            except Exception as e:
                db.rollback()
                raise

