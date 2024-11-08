from typing import Callable, Any

from proto import article_pb2, article_pb2_grpc
import grpc
from concurrent import futures
from grpc_interceptor import ServerInterceptor


# 拦截器
class MyInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        print('my 拦截开始')
        print(continuation)
        print(handler_call_details)
        next_handler = continuation(handler_call_details)
        print("my 拦截结束")
        return next_handler

class YourInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        print('your 拦截开始')
        next_handler = continuation(handler_call_details)
        print("your 拦截结束")
        return next_handler


class AuthenticateInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        metadata = dict(handler_call_details.invocation_metadata)
        # 验证用户的逻辑：在元数据中寻找authorization，并且这个值为zhiliao
        if 'authorization' in metadata and metadata['authorization'] == 'zhiliao':
            return continuation(handler_call_details)
        else:
            # 也是要返回一个method_handler对象
            def terminate(request, context):
                context.abort(grpc.StatusCode.UNAUTHENTICATED, '请传入Token！')
            return grpc.unary_unary_rpc_method_handler(terminate)


class UserInterceptor(ServerInterceptor):
    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        context: grpc.ServicerContext,
        method_name: str,
    ) -> Any:
        context.user = self.user
        return method(request_or_iterator, context)

    def intercept_service(self, continuation, handler_call_details):
        metadata = dict(handler_call_details.invocation_metadata)
        # 验证用户的逻辑：在元数据中寻找authorization，并且这个值为zhiliao
        if 'authorization' in metadata and metadata['authorization'] == 'zhiliao':
            # 从数据库中查找用户数据
            self.user = {"id": 1, 'username': 'zhiliao'}
        else:
            self.user = None
        return super().intercept_service(continuation, handler_call_details)


class ArticleService(article_pb2_grpc.ArticleServiceServicer):
    def ArticleList(self, request, context):
        print("user:", context.user)
        response = article_pb2.ArticleListResponse()
        articles = [
            article_pb2.Article(id=1, title='xx', content='yy', create_time='2030-10-10')
        ]
        response.articles.extend(articles)
        return response

def main():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        # interceptors=[MyInterceptor(), YourInterceptor()]
        # interceptors=[AuthenticateInterceptor()]
        interceptors=[UserInterceptor()]
    )
    article_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleService(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()