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
        print("Entrando a UserServices.create_user")
        return self.user_repository.create_user(nuevo_usuario)
        

