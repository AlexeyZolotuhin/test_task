import typing
from fastapi import APIRouter
from app.employees.models import Employee
from app.web.utils import json_response

if typing.TYPE_CHECKING:
    from app.web.app import FastAPI

router = APIRouter()


def setup_routes(app: "FastAPI"):
    @router.get("/employees")
    async def get_list_employees(body: Employee):
        res = await app.store.employees.get_list_employees(params=body.dict(exclude_none=True, by_alias=True))
        # TODO надо бы использовать JSONResponse из fastapi, а не своЙ
        return json_response(data=res)

    app.include_router(router)

