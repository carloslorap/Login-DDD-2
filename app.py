# app.py

from flask import Flask
from flask_cors import CORS

# Importar conexión a base de datos
from app.infrastructure.db.connection import engine, Base
# Importar rutas
from app.infrastructure.web.routes.auth_routes import auth_bp
from app.infrastructure.web.routes.user_routes import user_bp
from app.infrastructure.web.routes.solicitud_routes import solicitudes_bp
from app.infrastructure.web.routes.dashboard_routes import dashboard_bp

from app.infrastructure.email import mail
from app.config.settings import settings
from app.web.context import inject_role_helpers
from app.web.middleware import register_session_sanitizer


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = settings.SECRET_KEY

  
 
 # Context processor (variables para todas las plantillas)
app.context_processor(inject_role_helpers)

# Middleware (saneado de cookie)
register_session_sanitizer(app)
 
 
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
app.register_blueprint(dashboard_bp)

# Crear las tablas en la base de datos si no existen
with app.app_context():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app.run(debug=True)
