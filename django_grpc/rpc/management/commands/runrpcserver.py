from django.core.management.base import BaseCommand
from article.models import Article as ArticleModel
from rpc import article_pb2, article_pb2_grpc
import grpc
import asyncio

class ArticleService(article_pb2_grpc.ArticleServiceServicer):
    async def ArticleList(self, request, context):
        page = request.page
        page_size = request.page_size
        print('page:', page, "page_size:", page_size)
        response = article_pb2.ArticleListResponse()
        articles = []
        queryset = ArticleModel.objects.all()
        async for article in queryset:
            articles.append(article_pb2.Article(
                id=article.id,
                title=article.title,
                content=article.content,
                create_time=article.create_time.strftime("%Y-%m-%d")
            ))
        # 以下代码是错误的
        # response.articles = articles
        response.articles.extend(articles)
        return response


class Command(BaseCommand):
    async def start(self):
        # 1. 创建一个grpc服务器对象
        server = grpc.aio.server()
        # 2. 将文章服务，添加到server服务器中
        article_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleService(), server)
        # 3. 绑定ip和端口号
        server.add_insecure_port("0.0.0.0:5000")
        # 4. 启动服务
        await server.start()
        print('gRPC服务器已经启动！监听：0.0.0.0:5000')
        # 5. 死循环，等待关闭
        await server.wait_for_termination()

    def handle(self, *args, **options):
        asyncio.run(self.start())