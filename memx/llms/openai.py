from __future__ import annotations

import typing

import openai

import memx._utils.kwargs as _kw
from memx.llms import _base


class OpenAI(_base.LLMs):

    def __init__(
        self,
        *,
        model: str,
        api_key: str,
        base_url: str,
        max_context_length: int,
        **kwargs: typing.Any
    ):
        self._model = model
        self._max_context_length = max_context_length
        self.client = openai.AsyncOpenAI(
            api_key=api_key,
            base_url=base_url,
            **_kw.filter_kwargs(openai.AsyncOpenAI.__init__, kwargs)
        )

    async def init(self) -> None:
        pass

    async def exec(self, text: str, **kwargs: typing.Any) -> str:
        pass

    async def exec_structured(
        self,
        text: str,
        *,
        schema: typing.Type[typing.TypedDict],
        **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]:
        pass

    async def close(self) -> None:
        pass
