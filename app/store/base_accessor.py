import typing

if typing.TYPE_CHECKING:
    from app.web.app import FastAPI


class BaseAccessor:
    def __init__(self, app: "FastAPI"):
        self.app = app
