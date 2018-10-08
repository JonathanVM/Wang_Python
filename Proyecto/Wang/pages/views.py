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
    submitted = False
    if request.method == 'POST':
        form = ProbarForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['cadena'],
                connection=con
            )
        else:
            form = ProbarForm()
            if 'submitted' in request.GET:
                submitted = True
    
        return render(request,
                      'pages/consulta.html',
                      {'form': form,
                      'page_list': Page.objects.all(),
                      'submitted': submitted})
    
    
    
    
    
    
    
    
    
    
    
    
    
    