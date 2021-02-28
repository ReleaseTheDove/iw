import orjson


class Redis:

    @classmethod
    def __init__(cls, redis):
        cls.redis = redis

    @classmethod
    async def set(cls, key, value, expire=0):
        return await cls.redis.set(key, orjson.dumps(value), expire=expire)

    @classmethod
    async def get(cls, key):
        res = await cls.redis.get(key)
        if res:
            return orjson.loads(res)
