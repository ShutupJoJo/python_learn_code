from django.core.management.base import BaseCommand
from article.models import Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        articles = []
        for x in range(10):
            title = f"title_{x}"
            content = f"content_{x}"
            articles.append(Article(title=title, content=content))
        Article.objects.bulk_create(articles)
        print("文章测试数据添加成功！")