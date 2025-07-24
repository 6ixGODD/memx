import importlib as _importlib
import typing as _t

from memx._version import (
    __title__,
    __version__,
)

__all__ = [
    '__title__',
    '__version__',

    '_embedding',
    '_llm',
    '_mem',
    '_vector_store',

    'client',
    'errors',
    'types_'
]


def __getattr__(name: str) -> _t.Any:
    if name in __all__:
        return _importlib.import_module("." + name, __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
