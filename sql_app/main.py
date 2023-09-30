from fastapi import FastAPI

from .art_app.router import art

app = FastAPI()

app.include_router(art)
