from abc import ABC, abstractmethod
from typing import List
from app.domain.solicitud.solicitud import Solicitud
from typing import Optional
from datetime import datetime

class SolicitudRepository(ABC):

    @abstractmethod
    def listar_filtrado(
        self,
        nombre: Optional[str] = None,
        fecha_inicio: Optional[datetime] = None,
        fecha_fin: Optional[datetime] = None,
        atendidos:Optional[bool] = None,
        page: int = 1,
        per_page: int = 10,
    ) -> List[Solicitud]:
        pass
    
    @abstractmethod
    def aprobar_solicitud(
        self,
        solicitud_id: int,
        nuevo_estado_id: int,
        atendido: int,
        usuario: str,
    ) -> None:
        """Actualiza estado_solicitud_id y atendido."""
        pass
    
    @abstractmethod
    def desaprobar_solicitud(
        self,
        solicitud_id: int,
        nuevo_estado_id: int,
        atendido: int,
        usuario: str,
    ) -> None:
        """Actualiza estado_solicitud_id y atendido."""
        pass