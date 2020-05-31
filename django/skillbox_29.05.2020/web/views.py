from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

from mysite import settings
from web.models import Publication, Comment


def index(request):
    return render(request, "index.html")


def contacts(request):
    return render(request, "contacts.html")


def status(request):
    return HttpResponse("<h1>OK</h1>")


def publications(request):
    return render(request, "publications.html", {
        'publications': Publication.objects.all()
    })


def publication(request, number):
    elements = Publication.objects.filter(id=number)

    if request.method == "GET":
        try:
            element = model_to_dict(elements[0])
            return render(request, "publication.html", element)
        except IndexError:
            return redirect('/')
    else:
        pass


def publish(request):
    if request.method == "GET":
        return render(request, "publish.html")
    else:
        if request.POST["secret"] != settings.SECRET_KEY:
            return render(request, "publish.html", {
                "error": "Неверный ключ"
            })
        elif len(request.POST["name"]) is 0 :
            return render(request, "publish.html", {
                "error": "Название не может быть пустым"
            })
        elif len(request.POST["text"]) is 0 :
            return render(request, "publish.html", {
                "error": "Текст не может быть пустым"
            })
        else:
            Publication(
                name=request.POST["name"],
                date=datetime.now(),
                text=request.POST["text"].replace("\n", "<br>")
            ).save()
            return redirect("/publications")
