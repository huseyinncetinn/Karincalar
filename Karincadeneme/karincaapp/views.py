from django.shortcuts import render ,get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def search(request):

    adoKapi = Kategori.objects.filter(kategori = 'ado')
    celikKapi = Kategori.objects.filter(kategori= 'celik')
    icKapi = Kategori.objects.filter(kategori = 'icoda')

    urunler = ''
    searched = ''

    if request.GET.get('searched'):
        searched = request.GET['searched']
        urunler = Urun.objects.filter(
            Q(urunKodu__contains = searched) |
            Q(urunKategori__isim__contains = searched)
        )

    context = {
        'adoKapi' : adoKapi,
        'celikKapi' : celikKapi,
        'icKapi' : icKapi,
        'urunler' : urunler
    }

    return render(request , 'search.html' ,context)

def index(request):
    
    adoKapi = Kategori.objects.filter(kategori = 'ado')
    celikKapi = Kategori.objects.filter(kategori= 'celik')
    icKapi = Kategori.objects.filter(kategori = 'icoda')

    context = {
        'adoKapi' : adoKapi,
        'celikKapi' : celikKapi,
        'icKapi' : icKapi
    }
    
    return render(request , "index.html" , context)


def kategori(request,slug):

    kategori = get_object_or_404(Kategori , slug = slug)
    urunler = Urun.objects.filter(urunKategori = kategori)
    adoKapi = Kategori.objects.filter(kategori = 'ado')
    celikKapi = Kategori.objects.filter(kategori= 'celik')
    icKapi = Kategori.objects.filter(kategori = 'icoda')

    page = Paginator(urunler , 12)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page' : page,
        'urunler' : urunler,
        'kategori' : kategori,
        'adoKapi' : adoKapi,
        'celikKapi' : celikKapi,
        'icKapi' : icKapi,
        "link" : "kategori/"+str(slug)
    }

    return render(request, "kategori.html" , context)
    
def hakkimizda(request):

    adoKapi = Kategori.objects.filter(kategori = 'ado')
    celikKapi = Kategori.objects.filter(kategori= 'celik')
    icKapi = Kategori.objects.filter(kategori = 'icoda')

    context = {
        'adoKapi' : adoKapi,
        'celikKapi' : celikKapi,
        'icKapi' : icKapi,
        "link" : "hakkimizda/"
    }
   
    return render(request , "hakkimizda.html" ,context)

def iletisim(request):

    adoKapi = Kategori.objects.filter(kategori = 'ado')
    celikKapi = Kategori.objects.filter(kategori= 'celik')
    icKapi = Kategori.objects.filter(kategori = 'icoda')

    context = {
        'adoKapi' : adoKapi,
        'celikKapi' : celikKapi,
        'icKapi' : icKapi,
        "link" : "iletisim/"
    }
   
    return render(request , "iletisim.html",context)

def urunDetay(request , slug):

    urun = Urun.objects.get(slug=slug)

    adoKapi = Kategori.objects.filter(kategori = 'ado')
    celikKapi = Kategori.objects.filter(kategori= 'celik')
    icKapi = Kategori.objects.filter(kategori = 'icoda')

    context = {
        'adoKapi' : adoKapi,
        'celikKapi' : celikKapi,
        'icKapi' : icKapi,
        'urun' : urun,
        "link" : "urunDetay/"+str(slug)
    }

    return render(request, "urun-detay.html",context)

def page_not_found_view(request, exception):
    return render(request, '404.html')