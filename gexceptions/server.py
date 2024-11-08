from proto import article_pb2, article_pb2_grpc
import grpc
from concurrent import futures
import time


class ArticleService(article_pb2_grpc.ArticleServiceServicer):
    def ArticleList(self, request, context):
        time.sleep(4)
        response = article_pb2.ArticleListResponse()
        # context.set_code(grpc.StatusCode.NOT_FOUND)
        # context.set_details('您找的资源不存在！')
        return response

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    article_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleService(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()