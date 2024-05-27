from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from app.core.database import get_session
from app.services.urls import UrlService
from app.routers.urls import router as urls_router

app = FastAPI(title="Fast URL shortener", docs_url="/")
app.include_router(router=urls_router, prefix="/urls", tags=["urls"])


@app.get("/{short_code}/")
def read_original_url(short_code: str, session=Depends(get_session)):
    service = UrlService(session=session)
    original_url = service.get_original_url(short_code).original_url
    return RedirectResponse(original_url.unicode_string())
