from django.urls import path
from .import views

app_name = 'diary'

urlpatterns = [
    path("", views.index, name='index'), #/diaryのときに読まれるだけ
    path("add/", views.add, name='add'),
    #updateの後はpkにあるintなら何でも良いよ
    path("update/<int:pk>", views.update, name='update'),
    path("delete/<int:pk>", views.delete, name='delete'),
    path("detail/<int:pk>", views.detail, name='detail'),
]
