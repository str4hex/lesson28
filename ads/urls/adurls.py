from django.conf.urls.static import static
from django.urls import path

from ads.views import AdApiView, AdViewDetail, AdUpdateApiView, AdDestroyApiView, AdViewCreate
from lesson28 import settings

urlpatterns = [
                  path('', AdApiView.as_view()),
                  path('create/', AdViewCreate.as_view()),
                  path('<int:pk>/', AdViewDetail.as_view()),
                  path('<int:pk>/update/', AdUpdateApiView.as_view()),
                  path('<int:pk>/delete/', AdDestroyApiView.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
