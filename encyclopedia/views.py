from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util

class CreateEntityForm(forms.Form):
    title = forms.CharField(label = "Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_content(request,title):
    return render(request, "encyclopedia/wiki.html",{
        "title": title,
        "content": util.get_entry(title)
    })

def search(request):
    if request.method == "POST":
        searched = request.POST.get("q", "")
        result_list = []
        if util.get_entry(searched):
            return get_content(request,searched)
        else:
            for x in util.list_entries():
                if searched.lower() == x[:len(searched)].lower():
                    result_list.append(x)

    return render(request, "encyclopedia/search.html",{
        "result_list": result_list
    })

def create(request):
    if request.method == "POST":
        form = CreateEntityForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title,content)
        else:
            return render(request,"ecnyclopecia/create.html",{
                "form":form
            })

    return render(request, "encyclopedia/create.html",{
        "form": CreateEntityForm()
    })