# ~*~ coding: utf-8 ~*~

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('Nucs.urls')),
    url(r'^admin/', admin.site.urls),
   # url(r'^admin_tools/', include('admin_tools.urls')),
]
