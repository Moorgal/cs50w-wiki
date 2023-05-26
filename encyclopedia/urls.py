from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entrypage>", views.entry_page, name="entry_page"),
    path("search_page", views.search_page, name="search_page"),
    path("new_page", views.new_page, name="new_page"),
    path("save_page", views.save_page, name="save_page"),
    path("edit_page", views.edit_page, name="edit_page"),
    path("make_sure_page", views.make_sure_page, name="make_sure_page"),
    path("delete_page", views.delete_page, name="delete_page"),
    path("random_page", views.random_page, name="random_page")
]
