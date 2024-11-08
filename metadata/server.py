from proto import article_pb2, article_pb2_grpc
import grpc
from concurrent import futures


class ArticleService(article_pb2_grpc.ArticleServiceServicer):
    def ArticleList(self, request, context):
        # 元数据的操作，都是通过context去实现的
        # 1. 获取客户端上传来的元数据：context.invocation_metadata()
        # 2. 返回给客户端的元数据：context.set_trailing_metadata()
        for key, value in context.invocation_metadata():
            print(key, value)
        response = article_pb2.ArticleListResponse()
        articles = [
            article_pb2.Article(id=1, title='xx', content='yy', create_time='2030-10-10')
        ]
        context.set_trailing_metadata((
            ('allow', 'True'),
            ('status', 'Healthy')
        ))
        response.articles.extend(articles)
        return response

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    article_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleService(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()