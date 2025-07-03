from __future__ import annotations

import typing as t

import openai

import memx._utils.kwargs as _kw
from memx._embedding import _base


class OpenAI(_base.Embedding):

    def __init__(
        self,
        *,
        mid: str,
        dim: int,
        model: str,
        api_key: str,
        base_url: str,
        **kwargs: t.Any
    ):
        self._mid = mid
        self._dim = dim
        self.model = model
        self.client = openai.AsyncOpenAI(
            api_key=api_key,
            base_url=base_url,
            **_kw.filter_kwargs(openai.AsyncOpenAI, kwargs)
        )

    async def init(self) -> None:
        pass

    async def embed(self, text: str, **kwargs: t.Any) -> t.List[float]:
        response = await self.client.embeddings.create(
            model=self.model,
            input=text,
            **_kw.filter_kwargs(self.client.embeddings.create, kwargs)
        )
        if not response or not response.data or not response.data[0].embedding:
            raise ValueError("Failed to retrieve _embedding from OpenAI API")
        return response.data[0].embedding

    async def close(self):
        await self.client.close()
