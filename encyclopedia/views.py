from django.shortcuts import render
from django import forms
from django.http import HttpResponse

from . import util

class NewPage(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

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
        
    
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        form = NewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"].capitalize()
            content = form.cleaned_data["content"]
            check_if_exist = util.get_entry(title)
            if check_if_exist == None:
                util.save_entry(title, content)
                return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()})
            else:
                problem = "page already exist"
                return render(request, "encyclopedia/error.html",{
                    "error": problem
                })
        else:
            problem = "please fill entries"
            return render(request, "encyclopedia/error.html",{
                "error": problem
            })