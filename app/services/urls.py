import hashlib
from typing import Any

import base58
from sqlalchemy import select, exists

from app.core.exceptions.urls import UrlNotFoundError
from app.models.urls import URL
from app.schemas.urls import UrlReadSchema
from app.services.base import (
    SessionMixin,
)


class UrlDataManager(SessionMixin):
    def get_original_url(self, short_code: str) -> URL:
        """Read original URL from database."""
        select_stmt = select(URL).where(URL.short_code == short_code)
        with self.session as session:
            url = session.scalar(select_stmt)

        return url

    def exists(self, short_code: str) -> URL | None:
        select_stmt = exists().where(URL.short_code == short_code)
        with self.session as session:
            url = session.query(select_stmt).scalar()
        return url

    def create_url(self, original_url: str, short_code: str) -> URL:
        """Write a new URL to the database."""
        url = URL(original_url=original_url, short_code=short_code)
        with self.session as session:
            session.add(url)
            session.commit()
            session.refresh(url)
        return url


class UrlService(SessionMixin):
    def get_original_url(self, short_code: str) -> UrlReadSchema:
        """Get original url by short code."""
        url: URL = UrlDataManager(self.session).get_original_url(short_code)
        if url is None:
            raise UrlNotFoundError(short_code=short_code)
        return UrlReadSchema.model_validate(url)

    def create_url(self, original_url: str) -> UrlReadSchema:
        """Create new short url from long one"""
        short_code = self._convert_to_short_code(original_url=original_url)
        url = UrlDataManager(self.session).exists(short_code=short_code)
        if url is None:
            url: URL = UrlDataManager(self.session).create_url(original_url=original_url, short_code=short_code)
        return UrlReadSchema.model_validate(url)

    def _convert_to_short_code(self, original_url: str) -> str:
        """Convert original url to short code"""
        hashed_value = self._hash_url(original_url)
        short_code = self._convert_to_base58(hashed_value)
        return short_code.decode()[0:7]

    @staticmethod
    def _hash_url(value: str) -> bytes:
        """Hash input with sha-256"""
        return hashlib.sha256(value.encode()).digest()

    @staticmethod
    def _convert_to_base58(value: Any) -> bytes:
        """Convert input to base58"""
        return base58.b58encode(value)
