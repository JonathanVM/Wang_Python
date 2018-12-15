
'''
autores:
    Delia Hernandez Ruiz
    Jonathan Vasquez Mora
    Erick Hernandez Camacho
'''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Page
from django.http  import HttpResponse

def index(request, pagename):
    print(f"index recibe {pagename}")
    pagename = "/" + pagename
    the_page = Page.objects.get(permalink=pagename)
    context = {
        "title": the_page.title,
        "content": the_page.bodytext,
        "last_updated": the_page.update_date,
        "page_list": Page.objects.all()
    }
    return render(request, "pages/page.html", context)
    
    
    
    