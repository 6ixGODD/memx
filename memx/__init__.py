import importlib as _importlib
import typing as _typing

from memx._version import (
    __title__,
    __version__,
)

__all__ = [
    '__title__',
    '__version__',

    'adapter',
    'mem',
    'client',
    'types_'
]


def __getattr__(name: str) -> _typing.Any:
    if name in __all__:
        return _importlib.import_module("." + name, __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
