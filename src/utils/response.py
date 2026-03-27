from fastapi.responses import JSONResponse

def success_response(data: dict, status_code: int = 200):
    """Standard success response format"""
    return JSONResponse (
        status_code = status_code,
        content = {"data": data}
    )

def error_response(code: str, message: str, status_code: int = 400, details : dict = None):
    """Standard error response format"""
    content = {
        "error": {
            "code": code,
            "message": message
        }
    }

    if details:
        content["error"]["details"] = details
    return JSONResponse (
        status_code = status_code,
        content = content
    )

def paginated_response(data: list, page: int, limit: int, total: int):
    """Standard paginated response"""
    return JSONResponse (
        status_code = 200,
        content = {
            "data": data,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "pages": (total + limit - 1)        # limit
                
            }
        }
    )

