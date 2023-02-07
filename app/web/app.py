from typing import Optional
from app.web.config import setup_config
from fastapi import FastAPI as ApplicationFastAPI
from app.web.config import Config
from app.store import Store, Mongo, setup_store
from app.web.routes import setup_routes


class FastAPI(ApplicationFastAPI):
    mongodb: Optional[Mongo] = None
    config: Optional[Config] = None
    store: Optional[Store] = None


app = FastAPI()


def setup_app(config_path: str) -> FastAPI:
    setup_config(app, config_path)
    setup_store(app)
    setup_routes(app)
    return app
