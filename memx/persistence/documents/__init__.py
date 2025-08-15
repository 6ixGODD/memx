from __future__ import annotations

import abc
import datetime as dt
import typing as t

import beanie
import pydantic as pydt

import memx.utils as utils


class BaseDocument(beanie.Document):
    @classmethod
    def gen_id(cls) -> str | beanie.BeanieObjectId:
        return beanie.BeanieObjectId()

    id: t.Annotated[
        str | beanie.BeanieObjectId,
        beanie.Indexed(),
        pydt.Field(
            default_factory=BaseDocument.gen_id,
            alias="_id"
        )
    ]

    created_at: t.Annotated[
        dt.datetime,
        beanie.Indexed(),
        pydt.Field(default_factory=utils.utc_now)
    ]

    updated_at: t.Annotated[dt.datetime | None, beanie.Indexed()] = None

