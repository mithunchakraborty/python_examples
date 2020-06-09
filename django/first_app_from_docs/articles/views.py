from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'articles/index.html', context)
