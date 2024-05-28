from fastapi import APIRouter, Depends
from app.core.database import get_session
from app.schemas.urls import UrlReadSchema, UrlCreateSchema
from app.services.urls import UrlService

router = APIRouter()


@router.post("/create/", response_model=UrlReadSchema)
def create_url(url: UrlCreateSchema, session=Depends(get_session)):
    # service = UrlService(session=session)
    # return service.create_url(original_url=url.original_url.unicode_string())
    return UrlReadSchema(original_url=url.original_url.unicode_string(), id="1", short_code="sdfjsl")


@router.get("/{short_code}/", response_model=UrlReadSchema)
def read_original_url(short_code: str, session=Depends(get_session)):
    service = UrlService(session=session)
    return service.get_original_url(short_code=short_code)
