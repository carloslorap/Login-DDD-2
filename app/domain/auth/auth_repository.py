from abc import ABC, abstractmethod
from typing import Optional
from app.domain.auth.auth import Auth
# esto aplica sobre las opereaciones que necesita el usuario en la aplicacion
class AuthRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> Optional[Auth]:
        pass
    
    # @abstractmethod|
    # def save(self, user: User) -> User:
    #     pass
