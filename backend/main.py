from fastapi import FastAPI
from contextlib import asynccontextmanager
from utils.init_db import create_tables
from routers.auth import router1, router2
from fastapi.staticfiles import StaticFiles
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

@asynccontextmanager
async def lifespan(app: FastAPI) :
    #Initialize DB at start
    create_tables()
    yield # Seperation point 


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory= BASE_DIR / "frontend/static"), name="static")


app.include_router(router1)
app.include_router(router2)

# client --> router --> serive --> repository --> db
# client <-- router <-- serive <-- repository <-- db

