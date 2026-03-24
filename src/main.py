# src/main.py
from fastapi import FastAPI
from src.config import settings

app = FastAPI(
    title="API Dependency Graph Analyzer",
    description="Tracks microservice dependencies and predicts breaking changes",
    version="1.0.0"
)

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
