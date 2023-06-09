from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
import random
from . import util



class NewPage(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, entrypage):
    html = util.get_entry(entrypage)
    content = util.converter(html)
    return render(request, "encyclopedia/entrypage.html", {
        "title" : entrypage,
        "entrypage": content
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
            "entrypage": util.converter(util.get_entry(pages[0]))})
        elif len_pages > 1:
            return render(request, "encyclopedia/search_page.html",{
            "pages": pages})
        else:
            problem = "This page does not exist"
            return render(request, "encyclopedia/error.html",{
                "error": problem
            })
        
    
def new_page(request):
    if request.method == "GET":
        form  = NewPage()
        return render(request, "encyclopedia/new_page.html", {
            'form': form
        })
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
        
def edit_page(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html",{
            "title": title,
            "content": content
        })

def save_page(request):
        if request.method == "POST":
            form = NewPage(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"].capitalize()
                content = form.cleaned_data["content"]
                util.save_entry(title, content)
                return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()})

            else:
                problem = "please fill both entries"
                return render(request, "encyclopedia/error.html",{
                "error": problem
                })

def make_sure_page(request):
    if request.method == "POST":
        title = request.POST['make_sure']
        return render(request, "encyclopedia/make_sure.html", {
            "name": title
        })

def delete_page(request):
    if request.method == "POST":
        title = request.POST['delete']
        util.delete_entry(title)
        return redirect('index')

def random_page(request):
    pages = util.list_entries()
    entrypage = random.choice(pages)
    return render(request, "encyclopedia/entrypage.html", {
        "title" : entrypage,
        "entrypage": util.converter(util.get_entry(entrypage))
    })