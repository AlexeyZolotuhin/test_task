import typing
from dataclasses import dataclass
import yaml

if typing.TYPE_CHECKING:
    from app.web.app import FastAPI


@dataclass
class MongoConfig:
    mongo_url: str
    mongo_db: str


@dataclass
class Config:
    mongo: MongoConfig


def setup_config(app: "FastAPI", config_path: str):
    with open(config_path, 'r', encoding='utf-8') as f:
        raw_config = yaml.safe_load(f)

    app.config = Config(
        mongo=MongoConfig(
            mongo_url=raw_config['mongo_config']['mongo_url'],
            mongo_db=raw_config['mongo_config']['mongo_db']
        )
    )
