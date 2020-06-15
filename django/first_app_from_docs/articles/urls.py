from django.urls import path
from . import views


# /articles/ +
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail')
]