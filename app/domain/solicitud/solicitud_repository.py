from abc import ABC, abstractmethod
from typing import List
from app.domain.solicitud.solicitud import Solicitud
from typing import Optional
from datetime import datetime

class SolicitudRepository(ABC):
    # @abstractmethod
    # def listar(self) -> List[Solicitud]:
    #     pass 
    
    @abstractmethod
    def listar_filtrado(
        self,
        nombre: Optional[str] = None,
        fecha_inicio: Optional[datetime] = None,
        fecha_fin: Optional[datetime] = None
    ) -> List[Solicitud]:
        pass