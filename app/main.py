from fastapi import FastAPI


def create_app():
    _app = FastAPI()
    return _app


app = create_app()
