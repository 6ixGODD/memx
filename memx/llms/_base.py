from __future__ import annotations

import abc
import functools
import typing

_T = typing.TypeVar('_T', bound=typing.TypedDict)


class LLMs(abc.ABC):
    _max_context_length: int
    _model: str

    @functools.lru_cache(maxsize=None)
    @property
    def max_context_length(self) -> int:
        return self._max_context_length

    @functools.lru_cache(maxsize=None)
    @property
    def model(self) -> str:
        return self._model

    @abc.abstractmethod
    async def init(self) -> None:
        pass

    @abc.abstractmethod
    async def exec(self, text: str, **kwargs: typing.Any) -> str:
        pass

    @abc.abstractmethod
    async def exec_structured(
        self,
        text: str,
        schema: typing.Type[_T],
        **kwargs: typing.Any
    ) -> _T:
        pass

    @abc.abstractmethod
    async def close(self) -> None:
        pass
