from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# def greet(request, title):
#     return HttpResponse(f"Hello, {title}")

def entry_page(request, entrypage):
    return render(request, "encyclopedia/entrypage.html", {
        "entrypage": util.get_entry(entrypage)
    })