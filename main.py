import os

from app.web.app import setup_app

app = setup_app(
    config_path=os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "configs/config.yml")
)
