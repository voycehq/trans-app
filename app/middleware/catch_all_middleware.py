from fastapi import Request


async def catch_all_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        from app.logs import logger
        import traceback
        from fastapi import Response

        logger.error(exc, exc_info=True)
        traceback.print_exc()
        return Response("An error occurred. Contact an admin for assistance", status_code=500)
