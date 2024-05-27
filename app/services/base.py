from typing import (
    Any,
    List,
)

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Executable


class SessionMixin:
    """Provides instance of database session."""

    def __init__(self, session: Session) -> None:
        self.session = session


class BaseService(SessionMixin):
    """Base class for application services."""


# class BaseDataManager(SessionMixin):
#     """Base data manager class responsible for operations over database."""
#
#     def add_one(self, model: Any) -> None:
#         session.add(model)
#
#     def get_one(self, select_stmt: Executable) -> Any:
#         with self.session as session:
#             return session.scalar(select_stmt)
#
#     def get_all(self, select_stmt: Executable) -> List[Any]:
#         with self.session as session:
#             return list(session.scalars(select_stmt).all())
