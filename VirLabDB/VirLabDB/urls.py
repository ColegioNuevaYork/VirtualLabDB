
from django.conf.urls import url, include
from django.contrib import admin
from . import strings

admin.site.site_header = strings.nombre_administracion
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('Elements.urls')),
]
