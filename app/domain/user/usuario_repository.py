from abc import ABC, abstractmethod
from app.domain.user.usuario import User
# esto aplica sobre las opereaciones que necesita el usuario en la aplicacion
class UserRepository(ABC):

     @abstractmethod
     def create_user(self, user: User) -> User:
        pass

    