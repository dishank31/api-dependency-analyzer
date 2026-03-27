# src/main.py
from fastapi import FastAPI
from src.config import settings
from src.routes import auth, services, endpoints, ingestion, graph, analysis
from src.middleware.error_handler import (
    global_exception_handler,
    app_exception_handler,
    AppException
)

app = FastAPI(
    title="API Dependency Graph Analyzer",
    description="Tracks microservice dependencies and predicts breaking changes",
    version="1.0.0"
)

app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(AppException, app_exception_handler)

app.include_router(auth.router)
app.include_router(services.router)
app.include_router(endpoints.router)
app.include_router(graph.router)
app.include_router(analysis.router)

@app.get("/")
def root():
    return {
        "message": "API Dependency Graph Analyzer",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "environment": settings.ENVIRONMENT
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "api-dependency-analyzer",
        "version": "1.0.0"
    }
