from protos.book import book_pb2
from protos.book import book_pb2_grpc
import grpc
import asyncio


async def main():
    # 1. 使用上下文管理器创建一个channel对象
    async with grpc.aio.insecure_channel("127.0.0.1:5000") as channel:
        # 2. 要发起grpc请求，需要借助Stub对象
        stub = book_pb2_grpc.BookServiceStub(channel)
        # 3. 构建一个请求对象
        request = book_pb2.BookListRequest()
        request.page = 100
        # 4. 发起请求
        response = await stub.BookList(request)
        for book in response.books:
            print(book.type)


if __name__ == '__main__':
    asyncio.run(main())