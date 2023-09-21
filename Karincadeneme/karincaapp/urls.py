from django.urls import path
from .views import *

urlpatterns=[
    path("" , index , name="index"),
    path("kategori/<str:slug>" , kategori , name="kategori"),
    path("hakkimizda/" , hakkimizda , name="hakkimizda"),
    path("iletisim/" , iletisim , name="iletisim"),
    path("urunDetay/<str:slug>" , urunDetay , name="urunDetay"),
    path('search' , search , name='search')
]