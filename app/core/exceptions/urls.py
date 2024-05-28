from fastapi import HTTPException
from fastapi import status


class UrlNotFoundError(HTTPException):
    """Raised when the provided short_code is not in the database."""

    def __init__(self, short_code):
        self.short_code = short_code
        self.detail = f"There is no URL with {self.short_code} code"
        super().__init__(detail=self.detail, status_code=status.HTTP_404_NOT_FOUND)

    def __str__(self):
        return self.detail

    def __repr__(self):
        return f"UrlNotFoundError(short_code={self.short_code!r})"
