import hashlib

class PasswordHasher:
    def hash(self, password: str) -> str:
        """Genera el hash SHA-256 de la contraseña."""
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def verify(self, password: str, hashed_password: str) -> bool:
        """Verifica si el hash coincide con el guardado."""
        return self.hash(password) == hashed_password
