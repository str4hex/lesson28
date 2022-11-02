from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from category import urls as caturls
from lesson28 import settings
from user import urls as userurls
from user.views import LocationViewList

router = routers.SimpleRouter()
router.register('location', LocationViewList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cat/', include(caturls)),
    path('user/', include(userurls)),
    path('ad/', include('ads.urls.adurls')),
    path('selection/', include('ads.urls.selectionurls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
