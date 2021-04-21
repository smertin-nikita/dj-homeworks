from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    articles = Article.objects.prefetch_related('articletag_set').order_by(ordering)
    context = {'articles': articles}

    return render(request, template, context)
