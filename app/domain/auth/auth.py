from dataclasses import dataclass
from typing import Optional

@dataclass
class Auth:
    usuario_id: int
    usuario: str               
    contrasena: str           

    