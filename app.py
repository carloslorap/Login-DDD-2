# app.py

from flask import Flask
from flask_cors import CORS

# Importar conexión a base de datos
from app.infrastructure.db.connection import engine, Base
# Importar rutas
from app.infrastructure.web.routes.auth_routes import auth_bp
from app.infrastructure.web.routes.user_routes import user_bp
from app.infrastructure.web.routes.solicitud_routes import solicitudes_bp

from app.infrastructure.email import mail
from app.config.settings import settings

app = Flask(__name__)
CORS(app)
app.secret_key = "123456789"

# Config Flask-Mail
app.config.update(
    MAIL_SERVER=settings.SMTP_HOST,
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_USE_TLS=settings.SMTP_USE_TLS,
    MAIL_USERNAME=settings.SMTP_USER,
    MAIL_PASSWORD=settings.SMTP_PASS,
    MAIL_DEFAULT_SENDER=settings.SMTP_FROM,
)

mail.init_app(app)

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(solicitudes_bp)

# Crear las tablas en la base de datos si no existen
with app.app_context():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app.run(debug=True)
