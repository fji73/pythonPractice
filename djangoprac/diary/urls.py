from django.urls import path
from . import views

app_name = "diary"
urlpatterns = [
    # どんなパスか, 動かす関数, 名前
    path("", views.index, name="index"),
    path("page/create/", views.page_create, name="page_create"),
]