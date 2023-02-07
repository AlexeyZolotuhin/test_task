import typing
from typing import Optional, List

from motor.motor_asyncio import AsyncIOMotorClient

if typing.TYPE_CHECKING:
    from app.web.app import FastAPI


class Mongo:

    def __init__(self, app: "FastAPI"):
        self.db = AsyncIOMotorClient(app.config.mongo.mongo_url)[app.config.mongo.mongo_db]

    def _get_collection(self, name_collection: str):
        return self.db[name_collection]

    async def find_one_by_param(self, name_param: str, value: str, name_collection: str) -> Optional[dict]:
        document = await self._get_collection(name_collection).find_one({name_param: value})
        return document

    async def find_many_by_params(self, name_collection: str, params: dict):
        cursor = self._get_collection(name_collection).find(params)
        res: List = []
        async for document in cursor:
            res.append(document)
        return res
