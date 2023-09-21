from django.db import models
from django.utils.text import slugify



# Create your models here.


class Kategori(models.Model):
    kategoriler = [
        ('celik' , 'Çelik Kapı'),
        ('ado' , 'Ado Kapı'),
        ('icoda' , 'İç Oda Kapı')
    ]

    kategori = models.CharField(max_length=50 , choices=kategoriler)
    isim = models.CharField(max_length=50)
    kategoriResim = models.FileField(upload_to='kategoripic/')
    slug = models.SlugField(null=True , unique=True , db_index=True,blank=True,editable=False)
    backImage = models.FileField(upload_to='backgroundkategori' , null=True , blank=True)
    

    def save(self, *args , **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args , **kwargs)

    def __str__(self):
        return self.isim
    
    class Meta:
        verbose_name = "Kategorı"
        verbose_name_plural = "Kategorıler"
    
class Urun(models.Model):
    urunKodu = models.CharField(max_length=50)
    urunKategori = models.ForeignKey(Kategori ,on_delete = models.CASCADE , null=True)
    slug = models.SlugField(null=True , unique=True , db_index=True,blank=True,editable=False)
    urunResim = models.FileField(upload_to='urunpic/')
    urunResim2 = models.FileField(upload_to='urunpic/' , null=True ,blank=True)
    urunResim3 = models.FileField(upload_to='urunpic/' , null=True ,blank=True)
    urunResim4 = models.FileField(upload_to='urunpic/' , null=True ,blank=True)
    urunResim5 = models.FileField(upload_to='urunpic/' , null=True ,blank=True)
    urunResim6 = models.FileField(upload_to='urunpic/' , null=True ,blank=True)
    urunResim7 = models.FileField(upload_to='urunpic/' , null=True ,blank=True)
    urunResim8 = models.FileField(upload_to='urunpic/' , null=True ,blank=True)
    urunResim9 = models.FileField(upload_to='urunpic/' , null=True ,blank=True)
    urunResim10 = models.FileField(upload_to='urunpic/' , null=True ,blank=True)
    icDolgu = models.TextField(max_length=1000 , null=True ,blank=True)
    icKasa = models.TextField(max_length=1000 , null=True , blank=True)
    icPervaz = models.TextField(max_length=1000 , null=True , blank=True)
    icBoya = models.TextField(max_length=1000 , null=True , blank=True)
    icKanat = models.TextField(max_length=1000 , null=True , blank=True)
    icSerenler = models.TextField(max_length=1000 , null=True , blank=True)
    icMasif=models.TextField(max_length=2000 , null=True , blank=True)
    adoKanat = models.TextField(max_length=1000 , null=True , blank=True)
    adoKasaPervaz = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik1 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik2 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik3 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik4 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik5 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik6 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik7 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik8 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik9 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik10 = models.TextField(max_length=1000 , null=True , blank=True)
    celikicerik11 = models.TextField(max_length=1000 , null=True , blank=True)

    def save(self, *args , **kwargs):
        self.slug = slugify(self.urunKodu)
        super().save(*args , **kwargs)

    def __str__(self):
        return self.urunKodu

    
