from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Solicitud:
    """
    Entidad Solicitud - Representa una solicitud de cita médica.
    
    Attributes:
        solicitud_id: Identificador único de la solicitud
        jid_id: ID del JID que realizó la solicitud
        especialidad_id: ID de la especialidad solicitada
        nombres: Nombres del solicitante
        tipo_documento_id: ID del tipo de documento
        numero_documento: Número del documento
        telefono: Teléfono de contacto
        email: Correo electrónico
        continuador: Indica si es paciente continuador
        sis: Indica si tiene SIS
        atendido: Indica si fue atendido
        estado: Estado de la solicitud
        estado_solicitud_id: ID del estado de la solicitud
        usuario: Usuario que procesó la solicitud
        interconsulta: Indica si requiere interconsulta
        interconsulta_imagen: Imagen para interconsulta
        created_at: Fecha de creación
        updated_at: Fecha de última actualización
    """
    jid_id: int
    especialidad_id: int
    nombres: str
    tipo_documento_id: int
    numero_documento: str
    telefono: str
    email: str = ''
    continuador: bool = False
    sis: bool = False
    atendido: bool = False
    estado: bool = True
    estado_solicitud_id: int = 1
    usuario: Optional[str] = ''
    interconsulta: bool = False
    interconsulta_imagen: str = ''
    solicitud_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None