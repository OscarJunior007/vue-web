from fastapi import FastAPI
from pydantic import BaseModel
from app.adapters.download_yt import download

class linkAutorized(BaseModel):
    link:str

def get_link(app:FastAPI):


    @app.post("/api/obtener-link")
    def obtener_link(link:linkAutorized):
        print(link.link)
        download(link.link)
        