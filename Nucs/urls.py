from django.conf.urls import url, include, re_path

from . import views


MAC_ADDRESS_PATTERN = r'?([\dA-F]{2}(?:[-:][\dA-F]{2}){5})'

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^nucs/', views.main_page, name='main_page'),
    url(r'^nuc/%s' % MAC_ADDRESS_PATTERN, views.get_nucs, name='nuc_mac'),
]
