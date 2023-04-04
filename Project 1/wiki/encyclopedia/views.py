from django import forms
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import util
from django.urls import reverse
import random
import markdown2


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
      
# Create the views here.
def index(request): 
    # 1. If Using 'Search'
    if 'q' in request.GET and request.GET['q']:
        if util.get_entry(request.GET['q']) != None:
            for file in util.list_entries():
                if str.lower(request.GET['q']) in str.lower(file):
                    name = file
            return render(request, "encyclopedia/entry.html", {
                "entries": util.get_entry(request.GET['q']),
                "name": name
            })       
        else:
            # Create the list that contain the strings we search  
            files = []    
            for file in util.list_entries():
                if str.lower(request.GET['q']) in str.lower(file):
                    files.append(file)
            # Returns the list we created previously   
            return render(request, "encyclopedia/index.html", {
                "entries": files
            })
    # 2. Entering the site for first time
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()  
})

def entry(request,name):
    # 1. If path do not exist, return 404 error
    if util.get_entry(name) == None:
        raise Http404
    # Create the new variable for head name to make its letter case not affected by the typing of path
    for file in util.list_entries():
            if str.lower(name) == str.lower(file):
                Name = file
    # 2. Returns the entry page corresponding to the path
    return render(request, ("encyclopedia/entry.html"), {
        "entries": markdown2.markdown(util.get_entry(name)),
        "name": Name
})

def create(request):
    # 1. Create New Entry
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"].capitalize()
            content = request.POST['content']
            # If entry doesn't exists.
            if util.get_entry(title) == None:
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse("wikipedia:entry", args=[title]))
            #If entry already exists.
            else:
                return HttpResponse("Error. The entry already exists.")
    # 2. Entering the site for first time      
    return render(request, "encyclopedia/create.html", {
        "form": NewEntryForm()
    })
    
def edit(request,name):
    # 1. Edit the Entry
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_bound:
            content = request.POST['content']
            util.save_entry(name,content)
            return HttpResponseRedirect(reverse("wikipedia:entry", args=[name]))
    # 2. Entering the site for first time
    return render(request, "encyclopedia/edit.html", {
        "title": name,
        "content": util.get_entry(name)
    })
    
def randomPage(request):
    name = random.choice(util.list_entries())
    return render(request, "encyclopedia/entry.html", {
        "entries": markdown2.markdown(util.get_entry(name)),
        "name": name
    })