from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entrypage>", views.entry_page, name="entry_page")
    # path("wiki/<str:title>", views.greet, name="greet")
]


# path whatever
# if get_entry(link) === none show this
# else show link