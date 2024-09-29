import asyncio
import time
from functools import wraps, partial


def async_timed(func):
    @wraps(func)
    async def wrapped(*args, **kwargs):
        print(f'开始执行{func}，参数为：{args}, {kwargs}')
        start = time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.time()
            total = end - start
            print(f'结束执行{func}，耗时：{total:.4f}秒')

    return wrapped


def blocking_function():
    print('blocking开始')
    time.sleep(2)
    print('blocking结束')
    return "success"


async def task_will_fail():
    await asyncio.sleep(1)
    raise ValueError('发生异常啦！')


async def enternity(delay, what):
    await asyncio.sleep(delay)
    return what


def callback(delay, future):
    print('回调')
    print('delay:', delay)
    print('执行结果：', future.result())


async def main():
    print('main开始')
    task = asyncio.create_task(enternity(1, 'hello'))
    task.add_done_callback(partial(callback, 2))
    await task
    print('main结束')


if __name__ == "__main__":
    asyncio.run(main())