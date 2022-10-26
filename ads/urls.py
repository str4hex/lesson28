from django.conf.urls.static import static
from django.urls import path

from lesson28 import settings


urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

