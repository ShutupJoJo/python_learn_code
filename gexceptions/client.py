import grpc
from proto import article_pb2, article_pb2_grpc

def main():
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = article_pb2_grpc.ArticleServiceStub(channel)
        request = article_pb2.ArticleListRequest(page=1)
        try:
            # response = stub.ArticleList(request)
            response = stub.ArticleList(request, timeout=2)
            print(response.articles)
        except grpc.RpcError as e:
            print(e.code())
            print(e.details())


if __name__ == '__main__':
    main()

