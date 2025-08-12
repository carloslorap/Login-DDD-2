from sqlalchemy import Column, Integer, String, Boolean
from app.infrastructure.db.connection import Base

class EspecialidadModel(Base):
    __tablename__ = "tbl_especialidad"  # nombre real de tu tabla en la BD

    especialidad_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    estado = Column(Boolean, default=True)
