from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Solicitud:
    jid_id: int
    especialidad_id: int
    
    nombres: str
    tipo_documento_id: int
    numero_documento: str
    telefono: str
    email: str
    continuador: bool
    sis: bool
    atendido: bool
    estado: bool
    estado_solicitud_id: int
    interconsulta: bool
    interconsulta_imagen: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    solicitud_id: Optional[int]
    usuario: Optional[str]
    especialidad_nombre: Optional[str]  # <- nombre de la especialidad
