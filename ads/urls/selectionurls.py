from django.conf.urls.static import static
from django.urls import path

from ads.views import AdApiView, AdViewDetail, AdUpdateApiView, AdDestroyApiView, AdViewCreate, SelectionCreateApiView, \
    SelectionDetailApiView, SelectionUpdateApiView, SelectionDeleteApiView, SelectionListApiView
from lesson28 import settings

urlpatterns = [
                  path('', SelectionListApiView.as_view()),
                  path('create/', SelectionCreateApiView.as_view()),
                  path('<int:pk>/', SelectionDetailApiView.as_view()),
                  path('<int:pk>/update/', SelectionUpdateApiView.as_view()),
                  path('<int:pk>/delete/', SelectionDeleteApiView.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
