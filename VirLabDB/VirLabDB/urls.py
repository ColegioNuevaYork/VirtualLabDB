
from django.conf.urls import url, include
from django.contrib import admin

from . import strings
from django.conf import settings
from django.conf.urls.static import static 

admin.site.site_header = strings.nombre_administracion
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('Elements.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
