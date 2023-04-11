import asyncio, functools
from typing import Any


class XWrapper:

    async def async_function(self, func, *args, **kwargs):
        return await func(*args, **kwargs)

    def sync_function(self, func, *args, **kwargs):
        return func(*args, **kwargs)

    def __call__(self, func):
        if asyncio.iscoroutinefunction(func):
            @functools.wraps(func)
            async def async_wrapper(*args: Any, **kwargs: Any):
                return self.async_function(func, *args, **kwargs)

            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args: Any, **kwargs: Any):
                return self.sync_function(func, *args, **kwargs)

            return sync_wrapper