from abc import ABC, abstractmethod
from typing import List
from app.domain.solicitud.respuesta_solicitud import RespuestaSolicitud

class RespuestaSolicitudRepository(ABC):
    @abstractmethod
    def listar_por_estado(self, estado_solicitud_id: int) -> List[RespuestaSolicitud]:
        pass