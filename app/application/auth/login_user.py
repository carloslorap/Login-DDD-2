from app.domain.auth.auth_repository import AuthRepository
from app.infrastructure.auth.password_hasher import PasswordHasher
from flask import flash

class LoginUser:
    def __init__(self, user_repository: AuthRepository, password_hasher: PasswordHasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, username: str, password: str): 
        # Buscar usuario por su nombre de usuario (login)
        user = self.user_repository.get_by_username(username)

        if user is None:
            raise ValueError("Usuario no encontrado.")

        # Verificar la contraseña (hasheada)
        if not self.password_hasher.verify(password, user.contrasena):
            raise ValueError("Contraseña incorrecta.")

        return user
    

