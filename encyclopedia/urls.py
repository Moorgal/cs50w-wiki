from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entrypage>", views.entry_page, name="entry_page"),
    path("search_page", views.search_page, name="search_page"),
]
