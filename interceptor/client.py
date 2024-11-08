import grpc
from proto import article_pb2, article_pb2_grpc

# 客户端拦截器
class ClientInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request):
        print('拦截开始')
        next_handler = continuation(client_call_details, request)
        print('拦截结束')
        return next_handler


def main():
    with grpc.insecure_channel("localhost:5000") as channel:
        intercept_channel = grpc.intercept_channel(channel, ClientInterceptor())
        stub = article_pb2_grpc.ArticleServiceStub(intercept_channel)
        request = article_pb2.ArticleListRequest(page=1)
        metadata = (
            ('authorization', 'zhiliao'),
        )
        response, call = stub.ArticleList.with_call(request, metadata=metadata)
        print(response.articles)


if __name__ == '__main__':
    main()

