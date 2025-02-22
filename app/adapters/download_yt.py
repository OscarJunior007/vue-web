from pytubefix import YouTube
from pytubefix.cli import on_progress
from fastapi import HTTPException

def download(url):
    try:

        yt = YouTube(url, on_progress_callback=on_progress)
        titulo = yt.title

        ys = yt.streams.get_audio_only()
        ys.download()
        
        if ys:
            return ys
        raise HTTPException(status_code=200, detail=f"Video descargado con exito")
    
    except Exception as e:
        raise HTTPException(status_code=408, detail=f"NO SE PUDO DESCARGAR EL VIDEO {e}")