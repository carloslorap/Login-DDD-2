from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.infrastructure.db.connection import Base

class SolicitudModel(Base):
    __tablename__ = "tbl_solicitud"

    solicitud_id = Column(Integer, primary_key=True, autoincrement=True)
    jid_id = Column(Integer, ForeignKey("tbl_jid.jid_id"))
    especialidad_id = Column(Integer, ForeignKey("tbl_especialidad.especialidad_id"))
    nombres = Column(String(100))
    tipo_documento_id = Column(Integer, ForeignKey("tbl_tipo_documento.tipo_documento_id"))
    numero_documento = Column(String(20))
    telefono = Column(String(20))
    email = Column(String(100))
    continuador = Column(Boolean)
    sis = Column(Boolean)
    atendido = Column(Boolean)
    estado = Column(Boolean)
    estado_solicitud_id = Column(Integer, ForeignKey("tbl_estado_solicitud.estado_solicitud_id"))
    usuario = Column(String(50))
    interconsulta = Column(Boolean)
    interconsulta_imagen = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
