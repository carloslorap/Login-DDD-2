from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db.connection import Base
from datetime import datetime

class TipoUsuario(Base):
    __tablename__ = "tbl_tipo_usuario"

    tipo_usuario_id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    nombre = Column(String(50))
    estado = Column(String(10))

    usuarios = relationship("Usuario", back_populates="tipo_usuario")


class Usuario(Base):
    __tablename__ = "tbl_usuario"

    usuario_id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    usuario = Column(String(50))
    contrasena = Column(String(255))
    nombres = Column(String(100))
    ap_paterno = Column(String(50))
    ap_materno = Column(String(50))
    tipo_usuario_id = Column(Integer, ForeignKey("tbl_tipo_usuario.tipo_usuario_id"))
    estado = Column(String(10))

    tipo_usuario = relationship("TipoUsuario", back_populates="usuarios")
