from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

settings = get_settings()

SQLALCHEMY_DATABASE_URL = settings.database.DATABASE_DSN

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionFactory = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def get_session():
    """Create new database session."""

    session = SessionFactory()

    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
