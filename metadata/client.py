import grpc
from proto import article_pb2, article_pb2_grpc
# from grpc._server import _Context

def main():
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = article_pb2_grpc.ArticleServiceStub(channel)
        request = article_pb2.ArticleListRequest(page=1)
        metadata = (
            ('username', "zhiliao"),
            ('token', 'abc')
        )
        # 调用RPC接口的时，不再是直接调用，而是通过with_call函数调用，然后把metadata传过去
        response, call = stub.ArticleList.with_call(request, metadata=metadata)
        print(response.articles)
        # 获取服务端返回的元数据，通过call.trailing_metadata来获取
        print('从服务端获取到的元数据：')
        for key, value in call.trailing_metadata():
            print(key, value)


if __name__ == '__main__':
    main()

