from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class DatabaseConfig(BaseModel):
    """Backend database configuration parameters."""

    DATABASE_DSN: str = "sqlite:///./fast_url.db"


class Config(BaseSettings):
    """API configuration parameters.

    Automatically read modifications to the configuration parameters
    from environment variables and ``.env`` file.
    """

    database: DatabaseConfig = DatabaseConfig()

    model_config = SettingsConfigDict(
        env_file=".env",
    )


@lru_cache
def get_settings():
    return Config()
