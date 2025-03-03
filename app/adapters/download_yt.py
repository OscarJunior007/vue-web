from pytubefix import YouTube
from pytubefix.cli import on_progress
from fastapi import HTTPException
from fastapi.responses import FileResponse
import tempfile
import os

def download(url: str):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        titulo = yt.title
        
 
        
        nombre_archivo = f"{titulo}.mp3"

        
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_path = temp_file.name
        temp_file.close()

     
        ys = yt.streams.get_audio_only()
        ys.download(output_path=os.path.dirname(temp_path), filename=os.path.basename(temp_path))

     
        if os.path.getsize(temp_path) == 0:
            raise HTTPException(status_code=500, detail="El archivo descargado está vacío")

       
       
        return FileResponse(temp_path, filename=nombre_archivo, media_type="audio/mpeg")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"NO SE PUDO DESCARGAR EL VIDEO: {e}")