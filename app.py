# app.py

from flask import Flask
from flask_cors import CORS

# Importar conexión a base de datos
from app.infrastructure.db.connection import engine, Base
# Importar rutas
from app.infrastructure.web.routes.auth_routes import auth_bp
from app.infrastructure.web.routes.user_routes import user_bp

app = Flask(__name__)
CORS(app)
app.secret_key = "123456789"

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

# Crear las tablas en la base de datos si no existen
with app.app_context():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app.run(debug=True)
