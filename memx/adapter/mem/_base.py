from __future__ import annotations

import abc


class MemAdapter(abc.ABC):

    @abc.abstractmethod
    async def init(self) -> None:
        pass

    @abc.abstractmethod
    async def close(self) -> None:
        pass
