from django.shortcuts import render
from django import forms
from django.http import HttpResponse

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
        entries = util.list_entries()
        pages = []
        for entry in entries:
            if form.lower() in entry.lower():
                pages.append(entry) 
        len_pages = len(pages)
        if len_pages == 1:
            return render(request, "encyclopedia/entrypage.html",{
            "entrypage": util.get_entry(pages[0])})
        elif len_pages > 1:
            return render(request, "encyclopedia/search_page.html",{
            "pages": pages})
        else:
            problem = "no cookie in the jar"
            return render(request, "encyclopedia/error.html",{
                "error": problem
            })
        
    
