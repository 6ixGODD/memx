from __future__ import annotations

import typing

import qdrant_client

from graphragx.adapter.vecs import _base


class Qdrant(_base.VectorAdapter):
    _dim: int

    @property
    def dim(self) -> int:
        return self._dim

    def __init__(
        self,
        *,
        dim: int,
        location: str | None = None,
        url: str | None = None,
        port: int | None = None,
        grpc_port: int | None = None,
        **kwargs: typing.Any
    ):
        self._dim = dim
        self._client = qdrant_client.QdrantClient(
            location=location,
            url=url,
            port=port,
            grpc_port=grpc_port,
            **kwargs
        )

    async def query(
        self,
        query: str | typing.List[float],
        *,
        emb: typing.Callable[[str], typing.List[float]] | None = None,
        k: int = 10,
        **kwargs: typing.Any
    ):
        pass

    async def close(self):
        pass
