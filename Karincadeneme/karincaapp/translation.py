from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Kategori)
class KategoriTranslationOptions(TranslationOptions):
    fields = ('isim',)


@register(Urun)
class UrunTranslationOptions(TranslationOptions):
    fields = ('urunKodu','icDolgu' , 'icKasa' , 'icPervaz' , 'icBoya' , 'icKanat' , 'icSerenler' , 'icMasif' ,'adoKanat' , 'adoKasaPervaz' , 
              'celikicerik1' , 'celikicerik2' , 'celikicerik3' , 'celikicerik4' ,'celikicerik5','celikicerik6','celikicerik7',
              'celikicerik8','celikicerik9' , 'celikicerik10','celikicerik11')