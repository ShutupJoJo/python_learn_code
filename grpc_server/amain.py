import article_pb2
import article_pb2_grpc
# pip install grpcio
import grpc
import asyncio



class ArticleService(article_pb2_grpc.ArticleServiceServicer):
    async def ArticleList(self, request, context):
        page = request.page
        page_size = request.page_size
        print('page:', page, "page_size:", page_size)
        # 模拟：阻塞
        await asyncio.sleep(1)
        response = article_pb2.ArticleListResponse()
        articles = [
            article_pb2.Article(id=101, title='11', content='22', create_time='2030-10-10'),
            article_pb2.Article(id=102, title='xx', content='yy', create_time='2030-10-10'),
        ]
        # 以下代码是错误的
        # response.articles = articles
        response.articles.extend(articles)
        return response


async def main():
    # 1. 创建一个grpc服务器对象
    server = grpc.aio.server()
    # 2. 将文章服务，添加到server服务器中
    article_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleService(), server)
    # 3. 绑定ip和端口号
    server.add_insecure_port("0.0.0.0:5001")
    # 4. 启动服务
    await server.start()
    print('gRPC服务器已经启动！')
    # 5. 死循环，等待关闭
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(main())