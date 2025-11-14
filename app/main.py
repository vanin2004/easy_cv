import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router



app = FastAPI()

current_dir = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(current_dir, "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

app.include_router(router)