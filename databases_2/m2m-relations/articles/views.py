from django.db.models import Prefetch
from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleTag


def articles_list(request):
    template = 'articles/news.html'

    ordering = '-published_at'

    # queryset для тегов с инфой из промежуточной модели ArticleTag и основной Tag c сортировкой по главному тегу
    articletag_set = ArticleTag.objects.order_by('-major').select_related('tag')

    articles = Article.objects.order_by(ordering).prefetch_related(Prefetch('articletag_set', queryset=articletag_set))
    context = {'articles': articles}

    return render(request, template, context)
