from django.shortcuts import render
from . import util



# Create the views here.
def index(request):
    if request.method == "POST":
        
        return render(request, "encyclopedia/entry.hz", {
        "entries": util.get_entry()
})
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
})

def search(request):
    return render(request, "encyclopedia/layout.html", {
        "entries": util.get_entry()
})

