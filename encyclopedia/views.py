from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_content(request,title):
    return render(request, "encyclopedia/wiki.html",{
        "title": title,
        "content": util.get_entry(title)
    })