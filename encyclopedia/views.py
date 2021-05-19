from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdowner=Markdown()
    entryPage=util.get_entry(entry)
    if entryPage is None:
        return render(request,"encyclopedia/nonExistingEntry.html",{
            "entryTitle":entry
        })
    else :
        return render(request,"encyclopedia/entry.html",{
            "entry": markdowner.convert(entryPage),
            "entryTitle":entry
        })


