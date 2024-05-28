from urllib.parse import urlparse, parse_qsl, urlunparse, urlencode

from pydantic import BaseModel, Field, AnyUrl, ConfigDict, validator


class UrlReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    original_url: AnyUrl
    short_code: str = Field(max_length=7)


class UrlCreateSchema(BaseModel):
    original_url: AnyUrl
