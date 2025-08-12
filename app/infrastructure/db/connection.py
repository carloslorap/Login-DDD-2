from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.settings import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    echo=False,  # para ver las queries en consola (puedes quitarlo en producción)
    future=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
