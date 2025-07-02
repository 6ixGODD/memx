from __future__ import annotations

import abc


class MemDB(abc.ABC):

    @abc.abstractmethod
    async def init(self) -> None:
        pass

    @abc.abstractmethod
    async def close(self) -> None:
        pass
