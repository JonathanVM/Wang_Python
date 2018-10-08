from django.shortcuts import render

# Create your views here.

from django.http  import HttpResponse
from .models import Page

def index(request, pagename):
    #return HttpResponse("<h1>Hola</h1>")
    #return render(request, "base.html")
    #return render(request, "pages/page.html")
    pagename = "/" + pagename
    the_page = Page.objects.get(permalink=pagename)
    context = {
        "title": the_page.title,
        "content": the_page.bodytext,
        "last_updated": the_page.update_date
    }
    return render(request, "pages/page.html", context)