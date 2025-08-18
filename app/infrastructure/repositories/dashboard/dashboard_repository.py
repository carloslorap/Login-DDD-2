from app.infrastructure.db.connection import SessionLocal
from app.infrastructure.models.solicitud_model import SolicitudModel
from app.infrastructure.models.user_model import Usuario as UsuarioModel

class DashboardStatsRepository:
    def get_stats(self) -> dict:
        """
        Devuelve:
          - total_solicitudes: todas las solicitudes activas (estado=True)
          - total_pendientes: solicitudes activas con atendido == 0
          - total_atendidas: solicitudes activas con atendido == 1
          - usuarios_activos: usuarios con estado=True
        """
        with SessionLocal() as db:
            total_solicitudes = db.query(SolicitudModel).filter(SolicitudModel.estado == True).count()
            total_pendientes  = db.query(SolicitudModel).filter(SolicitudModel.estado == True,
                                                                SolicitudModel.atendido == 0).count()
            total_atendidas   = db.query(SolicitudModel).filter(SolicitudModel.estado == True,
                                                                SolicitudModel.atendido == 1).count()
            usuarios_activos  = db.query(UsuarioModel).filter(UsuarioModel.estado == True).count()

        return {
            "total_solicitudes": total_solicitudes,
            "total_pendientes": total_pendientes,
            "total_atendidas": total_atendidas,
            "usuarios_activos": usuarios_activos,
        }