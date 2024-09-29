import random


class AsyncPermission:
    async def has_permission(self, request, view) -> bool:
        if random.random() < 0.7:
            return False

        return True