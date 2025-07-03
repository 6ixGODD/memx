from __future__ import annotations

import abc
import functools
import typing as t


class Embedding(abc.ABC):
    _mid: str
    _dim: int

    @functools.lru_cache(maxsize=None)
    @property
    def mid(self) -> str:
        return self._mid

    @functools.lru_cache(maxsize=None)
    @property
    def dim(self) -> int:
        return self._dim

    @abc.abstractmethod
    async def init(self) -> None:
        pass

    @abc.abstractmethod
    async def embed(self, text: str, **kwargs: t.Any) -> t.List[float]:
        pass

    @abc.abstractmethod
    async def close(self) -> None:
        pass
