# 🏥 Gestor de Citas Médicas

Sistema de gestión de citas médicas desarrollado con **Arquitectura Hexagonal** usando Flask, SQLAlchemy y Microsoft SQL Server.

## 🏗️ Arquitectura

El proyecto implementa la **Arquitectura Hexagonal** (Puertos y Adaptadores) para separar la lógica de negocio de las tecnologías externas:


## 🚀 Características

- ✅ **Arquitectura DDD** - Separación clara de responsabilidades
- ✅ **Validación robusta** - Pydantic para DTOs
- ✅ **Base de datos** - Microsoft SQL Server con SQLAlchemy 2.0

## 📋 Funcionalidades

### 👥 Gestión de Pacientes
- Registro de pacientes con validación completa
- Consulta por documento o listado completo
- Actualización de datos personales

### 👨‍⚕️ Gestión de Médicos
- Registro de médicos con especialidades
- Consulta por especialidad o estado activo
- Gestión de disponibilidad

### 📅 Gestión de Citas
- Agendamiento con validación de disponibilidad
- Estados: Programada, Confirmada, En Curso, Completada, Cancelada
- Consultas por paciente, médico o fecha
- Confirmación y cancelación de citas

## 🛠️ Tecnologías

- **Backend**: Python 3.13+ con Flask
- **ORM**: SQLAlchemy 2.0+
- **Base de Datos**: Microsoft SQL Server
- **Validación**: Pydantic
- **Gestión de Dependencias**: uv

## 📦 Instalación

### Prerrequisitos
- Python 3.13+
- Microsoft SQL Server
- [uv](https://github.com/astral-sh/uv) (gestor de paquetes)

### Configuración

1. **Clonar el repositorio**
   ```bash
   git clone <repository-url>
   cd gestor-citas-medicas
   ```

2. **Crear entorno virtual**
   ```bash
   uv venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   uv pip install -r requirements.txt

   ```
3. **Instalar NodeModules**
   ```bash
   npm install
   ```

4. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tu configuración de base de datos
   ```

5. **Configurar base de datos**
   ```bash
   # Crear la base de datos 'citas_medicas' en SQL Server
   # Las tablas se crearán automáticamente al iniciar la aplicación
   ```

## 🚀 Ejecución

### Desarrollo
```bash
python run.py
```

### Estilos de (tailwind)
```bash
npm run wacth-css
```

### Producción
```bash
FLASK_DEBUG=False python run.py
```

La aplicación estará disponible en `http://localhost:5000`

## 🔧 Configuración

### Variables de Entorno

```env
# Base de Datos
DB_SERVER=localhost
DB_DATABASE=citas_medicas
DB_USERNAME=sa
DB_PASSWORD=tu_password
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_PORT=1433


## 🤝 Contribución

Por favor, lee [CONTRIBUTING.md](CONTRIBUTING.md) para conocer las guías de contribución y el proceso de desarrollo.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Equipo

Desarrollado siguiendo las mejores prácticas de arquitectura de software y principios SOLID.

---

**¡Gracias por usar el Gestor de Citas Médicas! 🏥**