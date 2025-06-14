from typing import Callable, Any
from django.views.generic.base import View

urls: list[tuple[str, Callable, str]] = []


def view(
    *,
    path: str | None = None,
    name: None | str = None,
    path_prefix: str = "",
):
    def inner(fn: Any):
        nonlocal name, path
        name = name or fn.__name__
        assert isinstance(name, str)

        if path is None:
            path = name

        path = path_prefix + path
        if isinstance(fn, type) and issubclass(fn, View):
            urls.append((path, fn.as_view(), name))
        else:
            urls.append((path, fn, name))
        return fn

    return inner