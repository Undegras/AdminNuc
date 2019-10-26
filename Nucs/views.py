# ~*~ coding: utf-8 ~*~

from django.http.response import HttpResponse
from django.shortcuts import Http404, render_to_response
from .models import Nucs, FFC
ffc_list = FFC.objects.all()

def main_page (request):
    # Получаем список постов
    nucs_list = Nucs.objects.all()

    # отрисовываем
    return render_to_response('list.html', {"nucs_list":  nucs_list, "ffc_list": ffc_list} )

def get_domain(self):
    nuc_domain = FFC.objects.filter(suff=self)
    return nuc_domain

def get_nucs (request, nuc_mac):
    try:
        # выбираем конкретный nuc по mac
        nuc = Nucs.objects.get(mac_addr_nuc=nuc_mac)
    except nuc.DoesNotExist:
        # если такого поста нет, то генерируем 404
        raise Http404

    # отрисовываем
    return render_to_response('single.html', {"title":  nuc.fqdn_name_nuc, "mac" : nuc.mac_addr_nuc, "ffc_list": ffc_list})