from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    usuario: str               
    contrasena: str           
    nombres: str
    ap_paterno: str
    ap_materno: str
    tipo_usuario_id: int
    estado: int = 1
    usuario_id: Optional[int] = None
    estado:Optional[bool]=True
    # estado: str
    