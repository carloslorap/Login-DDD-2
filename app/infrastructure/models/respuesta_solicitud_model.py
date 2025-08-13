# app/infrastructure/models/respuesta_solicitud_model.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.infrastructure.db.connection import Base

class RespuestaSolicitudModel(Base):
    __tablename__ = "tbl_respuesta_solicitud"

    respuesta_solicitud_id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # Ej.: "aprobado", "rechazado", "sin citas", etc.
    nombre = Column(String(100), nullable=False)

    # Texto que se autocompleta en el modal
    respuesta = Column(Text, nullable=False)

    # 2 = aprobado, 3 = rechazado (FK a tbl_estado_solicitud.estado_solicitud_id)
    estado_solicitud_id = Column(
        Integer, 
        ForeignKey("tbl_estado_solicitud.estado_solicitud_id"),
        nullable=False
    )

    # Activo/inactivo
    estado = Column(Integer, default=1, nullable=False)
