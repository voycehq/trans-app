from fastapi import Request


async def catch_all_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        from app.logs import logger
        from fastapi.responses import JSONResponse
        from fastapi import status
        from config import config

        response: dict = {
            "message": "An error occurred. Contact an admin for assistance",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
        }
        if config.ENV == "PROD":
            logger.error("An error occurred. Contact an admin for assistance")
        else:
            logger.error(exc, exc_info=True)
        return JSONResponse(content=response, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
