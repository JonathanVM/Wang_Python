from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request, pagename):
    #return HttpResponse("<h1> Consulta recibida </h1> ")
    pagename = "/" + pagename
    the_page = Page.objects.get(permalink=pagename)
    context = {
        "title": the_page.title,
        "content": the_page.bodytext,
        "last_updated": the_page.update_date
    }
    return render(request, "pages/page.html", context)
