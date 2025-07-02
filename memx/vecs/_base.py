from __future__ import annotations

import abc
import functools as fc
import typing as t 


class VectorStore(abc.ABC):
    _dim: int

    @fc.lru_cache(maxsize=None)
    @property
    def dim(self) -> int:
        return self._dim

    @abc.abstractmethod
    async def init(self) -> None:
        pass

    @t.overload
    async def query(
        self,
        query: str,
        *,
        emb: t.Callable[[str], t.List[float]],
        k: int = 10,
        **kwargs: t.Any
    ):
        pass

    @t.overload
    async def query(
        self,
        query: t.List[float],
        *,
        k: int = 10,
        **kwargs: t.Any
    ):
        pass

    @abc.abstractmethod
    async def query(
        self,
        query: t.Union[str, t.List[float]],
        *,
        emb: t.Callable[[str], t.List[float]] | None = None,
        k: int = 10,
        **kwargs: t.Any
    ):
        pass

    @abc.abstractmethod
    async def close(self) -> None:
        pass
