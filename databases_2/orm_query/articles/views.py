from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    defer = ['published_at', 'author__phone']
    articles = Article.objects.order_by(ordering).select_related('author', 'genre').defer(*defer)

    context = {'articles': articles}

    return render(request, template, context)
