from typing import List, Optional
from datetime import datetime
from app.domain.solicitud.solicitud import Solicitud
from app.domain.solicitud.solicitud_repository import SolicitudRepository

class SolicitudService:
    def __init__(self, repository: SolicitudRepository):
        self.repository = repository
    
    def listar_filtrado(
        self,
        nombre: Optional[str] = None,
        fecha_inicio: Optional[datetime] = None,
        fecha_fin: Optional[datetime] = None
    ) -> List[Solicitud]:
        return self.repository.listar_filtrado(nombre, fecha_inicio, fecha_fin)