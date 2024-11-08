from contextlib import asynccontextmanager
from fastapi import FastAPI
from loguru import logger
from utils.cache import TLLRedis
from utils.tll_consul import TLLConsul

tll_consul = TLLConsul()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.add("logs/file.logs", rotation="500 MB", enqueue=True, level='INFO')
    tll_consul.register()
    await tll_consul.fetch_user_service_addresses()
    yield
    # 程序即将结束之前，先把redis的连接关闭
    await TLLRedis().close()
    tll_consul.deregister()
