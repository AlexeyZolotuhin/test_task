import typing
from app.store.mongo.mongo import Mongo

if typing.TYPE_CHECKING:
    from app.web.app import FastAPI


class Store:
    def __init__(self, app: "FastAPI"):
        from app.store.employees.accessor import EmployeeAccessor

        self.employees = EmployeeAccessor(app)


def setup_store(app: "FastAPI"):
    app.mongodb = Mongo(app)
    app.store = Store(app)
