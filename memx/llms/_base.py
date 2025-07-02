from __future__ import annotations

import abc
import functools as fc
import typing as t

_T = t.TypeVar('_T', bound=t.TypedDict)


class LLMs(abc.ABC):
    _max_context_length: int
    _model: str

    @fc.lru_cache(maxsize=None)
    @property
    def max_context_length(self) -> int:
        return self._max_context_length

    @fc.lru_cache(maxsize=None)
    @property
    def model(self) -> str:
        return self._model

    @abc.abstractmethod
    async def init(self) -> None:
        pass

    @abc.abstractmethod
    async def exec(self, text: str, **kwargs: t.Any) -> str:
        pass

    @abc.abstractmethod
    async def exec_structured(
        self,
        text: str,
        schema: t.Type[_T],
        **kwargs: t.Any
    ) -> _T:
        pass

    @abc.abstractmethod
    async def close(self) -> None:
        pass
