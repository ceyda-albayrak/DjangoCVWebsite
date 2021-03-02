from django.db import models
from phone_field import PhoneField
from django.urls import reverse

# Create your models here.
class CV(models.Model):
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    image=models.ImageField(null=True, blank=True,upload_to='media/')
    name=models.CharField(max_length=100,verbose_name="İsim")
    surname=models.CharField(max_length=100,verbose_name="Soyisim")
    placeofbirth=models.CharField(max_length=100,verbose_name="Doğum Yeri")
    dateofbirth=models.DateField(verbose_name="Doğum Tarihi")
    maritalstatu=models.CharField(max_length=10,verbose_name="Medeni Hal")
    militarystatu=models.CharField(max_length=100,verbose_name="Askerlik Durumu")
    driverlicense=models.CharField(max_length=100,verbose_name="Sürücü Belgesi")
    job=models.CharField(max_length=100,verbose_name="Meslek")
    phone=PhoneField(blank=True, verbose_name="Telefon")
    email=models.EmailField(max_length=254,unique=True)
    address=models.TextField()
    website=models.URLField(blank=True)
    language=models.CharField(max_length=100,verbose_name="Dil")
    lgdegree=models.CharField(max_length=50,verbose_name="Deneyim")
    hobby=models.TextField()
    careerobjective=models.TextField(verbose_name="Kariyer Hedefi")
    university=models.CharField(max_length=250)
    department=models.CharField(max_length=250)
    unistartdate=models.DateField(verbose_name="Başlama Tarihi")
    uniduedate=models.DateField(verbose_name="Bitiş Tarihi")
    highschool=models.CharField(max_length=250)
    highstartdate=models.DateField(verbose_name="Başlama Tarihi")
    highduedate=models.DateField(verbose_name="Bitiş Tarihi")
    referencename=models.CharField(max_length=100,verbose_name="Referans İsim Soyisim",blank=True)
    referencephone=PhoneField(blank=True, verbose_name="Referans Telefon")
    ability=models.TextField(verbose_name="Yetenekler")

    def __str__(self):
        return self.name+self.surname

    def get_absolute_url(self):
        return reverse("view-cv", kwargs={"pk": self.pk})
       