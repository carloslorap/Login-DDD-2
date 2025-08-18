from typing import List
from app.domain.user.typeUser_repository import TipoUsuarioRepository
from app.domain.user.type_user import TipoUsuario
from app.domain.user.usuario_repository import UserRepository
from app.infrastructure.auth.password_hasher import PasswordHasher
from app.domain.user.usuario import User

class TypeUserServices:
    def __init__(self, tipo_usuario_repository: TipoUsuarioRepository):
        self.tipo_usuario_repository = tipo_usuario_repository

    def execute(self) -> List[TipoUsuario]:
        return self.tipo_usuario_repository.get_all()
    
class UserServices:
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
    
    # Registrar un nuevo usuario
    def register_user(
        self,
        nombres: str,
        ap_paterno: str,
        ap_materno: str,
        usuario: str,
        contrasena: str,
        tipo_usuario_id: int
    ) -> User:
        # Encriptar la contraseña
        hashed_password = self.password_hasher.hash(contrasena)

        # Crear la entidad User
        nuevo_usuario = User(
            nombres=nombres,
            ap_paterno=ap_paterno,
            ap_materno=ap_materno,
            usuario=usuario,
            contrasena=hashed_password,
            tipo_usuario_id=tipo_usuario_id
        )
        return self.user_repository.create_user(nuevo_usuario)
    
    def change_password(self, user_id: int, current_password: str, new_password: str) -> None:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise ValueError("Usuario no encontrado.")

        # validar contraseña actual contra el hash
        if not self.password_hasher.verify(current_password, user.contrasena):
            raise ValueError("La contraseña actual es incorrecta.")

        # longitud minima
        if len(new_password) < 6:
            raise ValueError("La nueva contraseña debe tener al menos 6 caracteres.")

        new_hash = self.password_hasher.hash(new_password)
        self.user_repository.update_password(user_id, new_hash)
        

