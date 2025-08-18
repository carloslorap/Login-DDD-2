from dataclasses import dataclass
from typing import Optional

@dataclass
class Auth:
    usuario_id: int
    nombres: str
    ap_paterno: str
    ap_materno: str
    usuario: str               
    contrasena: str
    tipo_usuario_id:bool     

    @property
    def full_name(self) -> str:
        """
        Retorna 'Nombres ApPaterno ApMaterno' ignorando vacíos/None.
        """
        partes = [self.nombres, self.ap_paterno, self.ap_materno]
        return " ".join(p.strip() for p in partes if p and p.strip())