from django.db import models


# Create your models here.
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Модели'
        verbose_name = 'Модель'

    def __str__(self):
        return self.name


class Ty_pe(models.Model):
    ty_pe = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Тип смесителей'
        verbose_name = 'Тип смесителя'

    def __str__(self):
        return self.ty_pe


class Mixer(models.Model):
    name = models.CharField(max_length=100)
    typ_e = models.ForeignKey(Ty_pe, on_delete=models.CASCADE)
    vin = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='static/media', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Смесители'
        verbose_name = 'Смеситель'

    def get_absolute_url(self):
        return reverse('about_mixer', kwargs={'id':self.id})
    def __repr__(self):
        return self.name


