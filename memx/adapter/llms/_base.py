from __future__ import annotations

import abc
import typing


class LLMAdapter(abc.ABC):

    @abc.abstractmethod
    async def exec(
        self,
        *,
        query: str,
        **kwargs: typing.Any
    ) -> str | typing.Dict[str, typing.Any]:
        pass
