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
        fecha_fin: Optional[datetime] = None,
        atendidos:Optional[bool]= None,
        page: int = 1,
        per_page: int = 10,
    ) -> List[Solicitud]:
        return self.repository.listar_filtrado(nombre, fecha_inicio, fecha_fin,atendidos, page, per_page)
    
    def aprobar(self, solicitud_id: int, usuario_actual: str) -> None:
        # 2 = ACEPTADO, atendido = 1
        self.repository.aprobar_solicitud(
            solicitud_id=solicitud_id,
            nuevo_estado_id=2,
            atendido=1,
            usuario=usuario_actual,
        )
        
    def desaprobar(self, solicitud_id: int, usuario_actual: str) -> None:
        # 3 = ACEPTADO, atendido = 1
        self.repository.desaprobar_solicitud(
            solicitud_id=solicitud_id,
            nuevo_estado_id=3,
            atendido=1,
            usuario=usuario_actual,
        )
    
    