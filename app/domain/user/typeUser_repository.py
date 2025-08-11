from abc import ABC, abstractmethod
from typing import List
from app.domain.user.type_user import TipoUsuario
# esto aplica sobre las opereaciones que necesita el usuario en la aplicacion
    
class TipoUsuarioRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[TipoUsuario]:
        pass
