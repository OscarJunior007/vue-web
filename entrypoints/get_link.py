from fastapi import FastAPI


def get_link(app):

    app = FastAPI()

    @app.get("/")
    def root():
        return "hola mundo"