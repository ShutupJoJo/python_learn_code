from .single import SingletonMeta
import redis.asyncio as redis


class TLLRedis(metaclass=SingletonMeta):
    SMS_CODE_PREFIX = 'sms_code_{}'

    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, db=0)

    async def set(self, key, value, ex=5*60*60):
        await self.client.set(key, value, ex)

    async def get(self, key):
        value = await self.client.get(key)
        if type(value) == bytes:
            return value.decode('utf-8')
        return value

    async def set_sms_code(self, mobile, code):
        await self.set(self.SMS_CODE_PREFIX.format(mobile), code)

    async def get_sms_code(self, mobile):
        code = await self.get(self.SMS_CODE_PREFIX.format(mobile))
        return code

    async def close(self):
        await self.client.aclose()
