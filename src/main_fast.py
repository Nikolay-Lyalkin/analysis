from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.core.settings import settings
from src.handlers.coffee import router as cofe_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown


# Сначала создаем app
app = FastAPI(
    title=settings.project_name,
    docs_url="/openapi",
    openapi_url="/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


app.include_router(cofe_router, prefix="", tags=["coffee"])
