from __future__ import annotations

import typing as t 

import qdrant_client

from memx._vector_store import _base


class Qdrant(_base.VectorStore):

    def __init__(
        self,
        *,
        dim: int,
        location: str | None = None,
        url: str | None = None,
        port: int | None = None,
        grpc_port: int | None = None,
        **kwargs: t.Any
    ):
        self._dim = dim
        self._client = qdrant_client.QdrantClient(
            location=location,
            url=url,
            port=port,
            grpc_port=grpc_port,
            **kwargs
        )

    async def init(self) -> None:
        pass

    async def query(
        self,
        query: str | t.List[float],
        *,
        emb: t.Callable[[str], t.List[float]] | None = None,
        k: int = 10,
        **kwargs: t.Any
    ):
        pass

    async def close(self):
        pass
