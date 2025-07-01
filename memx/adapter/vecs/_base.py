from __future__ import annotations

import abc
import typing


class VectorAdapter(abc.ABC):

    @abc.abstractmethod
    def dim(self) -> int:
        pass

    @typing.overload
    async def query(
        self,
        query: str,
        *,
        emb: typing.Callable[[str], typing.List[float]],
        k: int = 10,
        **kwargs: typing.Any
    ):
        pass

    @typing.overload
    async def query(
        self,
        query: typing.List[float],
        *,
        k: int = 10,
        **kwargs: typing.Any
    ):
        pass

    @abc.abstractmethod
    async def query(
        self,
        query: typing.Union[str, typing.List[float]],
        *,
        emb: typing.Callable[[str], typing.List[float]] | None = None,
        k: int = 10,
        **kwargs: typing.Any
    ):
        pass

    @abc.abstractmethod
    async def close(self) -> None:
        pass
