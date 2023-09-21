from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

class KategoriAdmin(admin.ModelAdmin):
    list_display = ( 'isim' ,'slug',)
    readonly_fields = ('slug',)

class UrunAdmin(admin.ModelAdmin):
    list_display = ( 'urunKodu' ,'slug',)
    readonly_fields = ('slug',)


# Register your models here.

@admin.register(Urun)
class UrunAdmin(TranslationAdmin):
    list_display = ( 'urunKodu' ,'slug',)

    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Kategori)
class KategoriAdmin(TranslationAdmin):

    list_display = ( 'isim' ,'slug',)

    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

