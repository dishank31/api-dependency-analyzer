from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

async def global_exception_handler(request: Request, exc: Exception):
    """Catch all unhandled exceptions"""
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse (
        status_code = 500,
        content = {
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "An unexpected error occurred"
            }
        }
    )

class AppException(Exception):
    """Custom exception for known errors"""
    def __init__(self, code: str, message: str, status_code: int = 400, details: dict = None):
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details

async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse (
        status_code = exec.status_code,
        content = {
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details
            }
        }
    )