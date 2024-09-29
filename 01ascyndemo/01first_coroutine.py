import asyncio
import time
from utils import async_timed


# 定义一个协程
@async_timed
async def main():
    print('hello')
    # 协程必须要等待，也就是必须要在前面加上await关键字，否则这个协程不会执行
    await asyncio.sleep(1)
    # time.sleep(1)
    # 在协程中，对于那些会发生阻塞的I/O代码，一定不能使用同步的，否则程序就会阻塞在这个同步代码，失去并发性
    print('world')


if __name__ == '__main__':
    # 创建一个协程对象
    # main()：这样并不是直接执行main函数，而是创建一个协程
    cor = main()
    # 要把协程丢到事件循环中才会执行
    asyncio.run(cor)
