from rest_framework.throttling import BaseThrottle
import random


class AsyncThrottle(BaseThrottle):
    async def allow_request(self, request, view):
        if random.random() < 0.7:
            return False
        return True

    def wait(self):
        return 3