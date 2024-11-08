from django.shortcuts import render
import grpc
from rpc import article_pb2, article_pb2_grpc
from django.http.response import JsonResponse

# Create your views here.
async def article_list(request):
    # 通过微服务调用文章列表
    async with grpc.aio.insecure_channel("127.0.0.1:5000") as channel:
        stub = article_pb2_grpc.ArticleServiceStub(channel)
        article_request = article_pb2.ArticleListRequest()
        article_request.page = 2
        article_request.page_size = 10
        response = await stub.ArticleList(request)
        articles = []
        for article in response.articles:
            articles.append({"id": article.id, "title": article.title, "content": article.content})
        return JsonResponse({"articles": articles})
