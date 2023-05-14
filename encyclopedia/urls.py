from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entrypage>", views.entry_page, name="entry_page"),
    path("search_page", views.search_page, name="search_page"),
    path("new_page", views.new_page, name="new_page"),
    path("edit_page", views.edit_page, name="edit_page")
]
