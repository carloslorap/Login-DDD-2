from abc import ABC, abstractmethod
from app.domain.user.usuario import User
from typing import Optional

# esto aplica sobre las opereaciones que necesita el usuario en la aplicacion
class UserRepository(ABC):

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Devuelve el usuario (incluye hash de contraseña) o None."""
        pass

    @abstractmethod
    def update_password(self, user_id: int, hashed_password: str) -> None:
        """Actualiza el hash de contraseña de un usuario."""
        pass
    
