from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
# Create your views here.

from django.http  import HttpResponse
from .models import Page
from .forms import ProbarForm

def index(request, pagename):
    #return HttpResponse("<h1>Hola</h1>")
    #return render(request, "base.html")
    #return render(request, "pages/page.html")
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
    
def expresion(request):
    #print(f"expression recibe request")
    #return HttpResponse("<h1>Yaho!!</h1>")
    submitted = False
    if request.method == 'POST':
        form = ProbarForm(request.POST)
        if form.is_valid():
            valor=''
            for key, value in request.POST.items():
                if  key == "cadena":
                    print(value)
                    valor = value
                

            return render(request,
                'pages/consulta.html',
                {'form': form,
                'page_list': Page.objects.all(),
                'submitted': submitted, 
                'respuesta': valor,
                'mensaje': "Exitosamente recibimos la siguiente consulta: "})  
            
    else:
        form = ProbarForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                'pages/consulta.html',
                {'form': form,
                'page_list': Page.objects.all(),
                'submitted': submitted})
                
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    