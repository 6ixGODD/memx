from __future__ import annotations

import beanie
import motor.motor_asyncio as motor

from memx._mems import _base


class Mongo(_base.MemDB):

    def __init__(
        self,
        *,
        uri: str,
        db: str,
    ):
        self.client = motor.AsyncIOMotorClient(uri)
        self.db = self.client[db]

    async def init(self) -> None:
        await beanie.init_beanie(
            self.db,
            document_models=[]
        )

    async def close(self) -> None:
        pass
