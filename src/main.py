from fastapi import FastAPI
from .routers import items
from logger_kit import app_logger, RequestLoggingMiddleware

app = FastAPI(title="FastAPI with Submodules")

app.add_middleware(RequestLoggingMiddleware, exclude_paths={"/health"})

app.include_router(items.router, prefix="/api/v1", tags=["items"])


@app.get("/")
async def root():
    app_logger.info("Root endpoint accessed")
    return {"message": "Welcome to FastAPI with Submodules example"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
