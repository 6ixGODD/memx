from __future__ import annotations

import functools
import inspect
import typing


@functools.lru_cache(maxsize=None)
def _get_func_params(func: typing.Callable) -> typing.Set[str]:
    return set(inspect.signature(func).parameters.keys())


def filter_kwargs(
    func: typing.Callable,
    kwargs: typing.Dict[str, typing.Any],
    prefix: str = ""
) -> typing.Dict[str, typing.Any]:
    """
    Filter out invalid keyword arguments for a given function by comparing the provided
    keyword arguments to the function's signature. Only valid keyword arguments are returned.

    Args:
        func: The function to filter keyword arguments for.
        kwargs: The keyword arguments to filter.
        prefix: The prefix to remove from keyword argument names before checking. Defaults to "".

    Returns:
        The filtered keyword arguments with valid parameter names only.
    """
    valid_params = _get_func_params(func)

    if prefix:
        # Remove prefix and filter
        filtered = {}
        for key, value in kwargs.items():
            if key.startswith(prefix):
                param_name = key[len(prefix):]
                if param_name in valid_params and param_name not in {"self", "cls"}:
                    filtered[param_name] = value
        return filtered
    else:
        # Direct filtering without prefix removal
        return {
            key: value
            for key, value in kwargs.items()
            if key in valid_params and key not in {"self", "cls"}
        }
