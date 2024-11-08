import article_pb2
import article_pb2_grpc
import grpc


def main():
    # 1. 使用上下文管理器创建一个channel对象
    with grpc.insecure_channel("127.0.0.1:5001") as channel:
        # 2. 要发起grpc请求，需要借助Stub对象
        stub = article_pb2_grpc.ArticleServiceStub(channel)
        # 3. 构建一个请求对象
        request = article_pb2.ArticleListRequest()
        request.page = 100
        request.page_size = 20
        # 4. 发起请求
        response = stub.ArticleList(request)
        for article in response.articles:
            print(article.id, article.title)


if __name__ == '__main__':
    main()