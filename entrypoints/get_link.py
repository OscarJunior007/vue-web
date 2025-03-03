from fastapi import FastAPI
from pydantic import BaseModel
from app.adapters.download_yt import download
from pytubefix import YouTube

class linkAutorized(BaseModel):
    link:str

def get_link(app:FastAPI):

    @app.post("/api/download")
    def obtener_link(link:linkAutorized):
        print(link.link)
        return download(link.link)
    

        