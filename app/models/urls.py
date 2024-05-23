from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from .mixins import TimeStampedMixin
from sqlalchemy import String, Integer


class Base(DeclarativeBase):
    pass


class URL(Base, TimeStampedMixin):
    __tablename__ = 'urls'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    original_url: Mapped[str] = mapped_column(String(length=2048), unique=True)
    short_code: Mapped[str] = mapped_column(String(length=7), unique=True)
