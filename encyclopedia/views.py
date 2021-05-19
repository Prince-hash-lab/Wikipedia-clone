from django.http.response import HttpResponse, HttpResponseRedirect
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


def random(request):
    entries=util.list_entries()
    randomEntry=secrets.choice(entries)
    return HttpResponseRedirect(reverse("entry",kwags={'entry':randomEntry}))

def search(request):
    value=request.GET.get('q','')
    if(util.get_entry(value) is not None):
        return HttpResponseRedirect(reverse("entry",kwags={'entry':value}))
    else:
        subStringEntries=[]
        for entry in util.list_entries():
            if value.upper() in entry.upper():
                subStringEntries.append(entry)
        return render(request,"encylopedia/index.html",{
            "entries" : subStringEntries,
            "search" : True,
            "value" : value
        })