
__all__ = ['cache', ]


from functools import wraps
from app.db import Redis


def cache(expire=60):
    def wrapper(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            key = [func.__module__, func.__name__]
            request = kwargs.get('request', None)
            if request:
                if (request.method != "GET" or
                    request.headers.get("Cache-Control") == "no-store"):
                    return await func(*args, **kwargs)
                key.append(request.client.host)
            key = '_'.join(key)
            res = await Redis.get(key) or await func(*args, **kwargs)
            await Redis.set(key, res, expire)
            return res

        return inner
    return wrapper
