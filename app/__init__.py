from app.models import *
from sqlalchemy.ext.declarative import declarative_base

Base_Model = declarative_base()


def create_app():
    from logging.config import dictConfig
    from fastapi.responses import JSONResponse
    from fastapi import FastAPI, status, Request
    from fastapi.staticfiles import StaticFiles
    from app.config.logger import LogConfig
    from config import config
    from app.utils.connection import engine

    dictConfig(LogConfig().dict())
    debug: bool = config.ENV != 'PROD'
    main_app = FastAPI(debug=debug)

    # Cors Middleware
    from starlette_context import plugins
    from fastapi.middleware.cors import CORSMiddleware
    from starlette_context.middleware import RawContextMiddleware
    from app.middleware.catch_all_middleware import catch_all_exceptions
    main_app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=["*"],
        allow_headers=["*"]
    )
    main_app.add_middleware(RawContextMiddleware, plugins=(
        plugins.RequestIdPlugin(), plugins.CorrelationIdPlugin()))
    main_app.middleware('http')(catch_all_exceptions)
    main_app.mount("/static", StaticFiles(directory="static"), name="static")

    # Routes

    # Override Validation Error
    from fastapi.exceptions import RequestValidationError

    @main_app.exception_handler(RequestValidationError)
    async def http_exception_handler(request, error):
        import json

        errors = list()
        for err in json.loads(error.json()):
            errors.append({err['loc'][-1]: err['msg']})
        message = f"{list(errors[0].keys())[0]} {list(errors[0].values())[0]}"
        return JSONResponse(content={'statusCode': status.HTTP_400_BAD_REQUEST, "message": message, "error": errors[0]},
                            status_code=status.HTTP_400_BAD_REQUEST)

    # Customer Exception
    from app.config.error_exception import ErrorException

    @main_app.exception_handler(ErrorException)
    async def custom_exception_handler(request: Request, exc: ErrorException):
        return JSONResponse(
            status_code=exc.status,
            content={"statusCode": exc.status, "message": exc.error}
        )

    Base_Model.metadata.create_all(bind=engine)

    return main_app
