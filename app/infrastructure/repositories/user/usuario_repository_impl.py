from typing import List
from app.domain.user.typeUser_repository import TipoUsuarioRepository
from app.domain.user.type_user import TipoUsuario
from app.infrastructure.models.user_model import TipoUsuario as TipoUsuarioModel
from app.infrastructure.models.user_model import Usuario as UsuarioModel
from app.infrastructure.db.connection import SessionLocal
from app.domain.user.usuario_repository import UserRepository
from app.domain.user.usuario import User

class TipoUsuarioRepositoryImpl(TipoUsuarioRepository):
    def get_all(self) -> List[TipoUsuario]:
        with SessionLocal() as db:
            rows = db.query(TipoUsuarioModel).all()
            return [
                TipoUsuario(tipo_usuario_id=row.tipo_usuario_id, nombre=row.nombre)
                for row in rows
            ]


class UserRepositoryImpl(UserRepository):
    def create_user(self, user: User) -> User:
        print("Insertando usuario en DB")
        with SessionLocal() as db:
            new_user = UsuarioModel(
                nombres=user.nombres,
                ap_paterno=user.ap_paterno,
                ap_materno=user.ap_materno,
                usuario=user.usuario,
                contrasena=user.contrasena,
                tipo_usuario_id=user.tipo_usuario_id,
                estado=user.estado
            )
            db.add(new_user)
            db.commit()
            print("Commit realizado")
            db.refresh(new_user)

            # Devuelve la entidad de dominio actualizada
            return User(
                # usuario_id=new_user.usuario_id,
                nombres=new_user.nombres,
                usuario=new_user.usuario,
                contrasena=new_user.contrasena,
                ap_paterno=new_user.ap_paterno,
                ap_materno=new_user.ap_materno,
                tipo_usuario_id=new_user.tipo_usuario_id,
                estado=user.estado
            )
            
