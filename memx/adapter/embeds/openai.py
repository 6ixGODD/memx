from __future__ import annotations

import typing

import openai

import memx._utils.kwargs as _kw
from memx.adapter.embeds import _base


class OpenAI(_base.EmbeddingAdapter):

    def __init__(
        self,
        *,
        mid: str,
        dim: int,
        model: str,
        base_url: str,
        api_key: str,
        **kwargs: typing.Any
    ):
        self._mid = mid
        self._dim = dim
        self.model = model
        self.client = openai.AsyncOpenAI(
            api_key=api_key,
            base_url=base_url,
            **_kw.filter_kwargs(openai.AsyncOpenAI, kwargs)
        )

    async def embed(self, text: str, **kwargs: typing.Any) -> typing.List[float]:
        response = await self.client.embeddings.create(
            model=self.model,
            input=text,
            **_kw.filter_kwargs(self.client.embeddings.create, kwargs)
        )
        if not response or not response.data or not response.data[0].embedding:
            raise ValueError("Failed to retrieve embedding from OpenAI API")
        return response.data[0].embedding

    async def close(self):
        await self.client.close()
