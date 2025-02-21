from entrypoints.get_link import get_link
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"),name="static")

get_link(app)



@app.get("/")
def root():
    return "hola mundo"

