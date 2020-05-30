from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

from mysite import settings


def index(request):
    return render(request, "index.html")


def contacts(request):
    return render(request, "contacts.html")


def status(request):
    return HttpResponse("<h1>OK</h1>")


publications_data = [{
        "id": 0,
        "name": "Первая публикация",
        "date": datetime.now(),
        "text": "Это текст<br><br> дадая"
    }, {
        "id": 1,
        "name": "Вторая публикация",
        "date": datetime.now(),
        "text": "Это текст<br><br> второй публикации"
    }
]


def publications(request):
    return render(request, "publications.html", {
        'publications': publications_data
    })


def publication(request, number):
    try:
        return render(request, "publication.html", publications_data[number])
    except:
        return redirect('/')


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
            publications_data.append({
                "id": len(publications_data),
                "name": request.POST["name"],
                "date": datetime.now(),
                "text": request.POST["text"].replace('\n', "<br>")
            })
            return redirect("/publications")
