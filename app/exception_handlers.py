from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from pymongo.errors import PyMongoError

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error": str(exc)},
    )

async def mongo_exception_handler(request: Request, exc: PyMongoError):
    return JSONResponse(
        status_code=500,
        content={"detail": "Database error", "error": str(exc)},
    )
