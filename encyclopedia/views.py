from django.shortcuts import render
from django import forms

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, entrypage):
    return render(request, "encyclopedia/entrypage.html", {
        "entrypage": util.get_entry(entrypage)
    })

def search_page(request):
    if request.method == "POST":
        form = request.POST['q']
    return render(request, "encyclopedia/entrypage.html", {
        "entrypage": form
    })
