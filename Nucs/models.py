# ~*~ coding: utf-8 ~*~

# импортируем класс модели
from django.db import models
# и админки
from django.contrib import admin

# Create your models here.
class FFC (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, default='', verbose_name='Наименование ФФЦ')
    suff = models.CharField(max_length=6, unique=True, verbose_name='Суффикс')
    domain = models.CharField(max_length=256, default='.market.yandex.net', verbose_name='Домен')
    def __str__(self):  # __unicode__ on Python 2
        return "%s" % (self.suff)

class Nucs (models.Model):
    fqdn_name_nuc = models.CharField(max_length=255, blank='', verbose_name='Имя NUC')
    # A4-34-D9-BA-5F-72
    mac_addr_nuc = models.CharField(max_length=18, verbose_name='mac адрес')
    ip_addr_nuc = models.CharField(max_length=36, verbose_name='IP адрес')
    ffc_code = models.ForeignKey(FFC, on_delete=models.CASCADE)
    enables_nuc = models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return "%s %s" % (self.fqdn_name_nuc, FFC.domain)

    class Meta:
        ordering = ('fqdn_name_nuc',)
        verbose_name = "Nuc"
        verbose_name_plural = "Nucs"



class TypeOfNucs (models.Model):
    Type = models.CharField(max_length=12)
    DisplayType = models.CharField(max_length=32)

class NucsAdmin(admin.ModelAdmin):
    # в таблице списка постов выводить только колонку title, если вы добавите еще одно имя поля, то и оно выведется
    list_display = ('fqdn_name_nuc', 'mac_addr_nuc', 'ip_addr_nuc', 'enables_nuc', 'ffc_code')

class FFCAdmin(admin.ModelAdmin):
    list_display = ('name', 'suff', 'domain')

# связываем эту модель с моделью PostAdmin
admin.site.register(Nucs, NucsAdmin)
admin.site.register(FFC, FFCAdmin)
