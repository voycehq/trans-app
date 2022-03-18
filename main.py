from app import create_app

app = create_app()
if __name__ == '__main__':
    import uvicorn
    from config import config

    port: int = int(config.PORT)
    if config.ENV == "PROD":
        uvicorn.run(app, port=port)
    else:
        uvicorn.run("main:app", reload=True, port=port)
