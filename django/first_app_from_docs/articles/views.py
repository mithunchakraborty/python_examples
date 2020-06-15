from django.shortcuts import render
from .models import Articles


def index(request):
    list_articles = Articles.objects.all()

    context = {
        'list_articles': list_articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, id):
    article = list_articles = Articles.objects.get(id=id)

    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
