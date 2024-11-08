from protos.book import book_pb2
from protos.book import book_pb2_grpc
# pip install grpcio
import grpc
import asyncio



class BookService(book_pb2_grpc.BookServiceServicer):
    async def BookList(self, request, context):
        page = request.page
        print('page:', page)
        # 模拟：阻塞
        await asyncio.sleep(1)
        response = book_pb2.BookListResponse()
        books = [
            book_pb2.Book(name='三国演义', type=book_pb2.BookType.STORY, tags={"Python": 24, "Java": 12}, realname='罗贯中'),
            book_pb2.Book(name='水浒传', type=book_pb2.BookType.LOVE, tags={"Python": 10, "Java": 100}, username='施耐庵'),
        ]
        # 以下代码是错误的
        # response.books = books
        response.books.extend(books)
        return response


async def main():
    # 1. 创建一个grpc服务器对象
    server = grpc.aio.server()
    # 2. 将文章服务，添加到server服务器中
    book_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    # 3. 绑定ip和端口号
    server.add_insecure_port("0.0.0.0:5000")
    # 4. 启动服务
    await server.start()
    print('gRPC服务器已经启动！')
    # 5. 死循环，等待关闭
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(main())