from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class RespuestaSolicitud:
    respuesta_solicitud_id: int
    nombre: str
    respuesta: str
    estado_solicitud_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    estado: Optional[bool] = True