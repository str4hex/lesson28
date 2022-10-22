from django.conf.urls.static import static
from django.urls import path

from ads import views
from lesson28 import settings

urlpatterns = [
    path('', views.AdsViewList.as_view()),
    path('<int:pk>/', views.AdsDetailView.as_view()),
    path("create/", views.AdCreateView.as_view()),
    path("<int:pk>/delete/", views.AdDeleteView.as_view()),
    path("<int:pk>/update/", views.AdUpdateView.as_view()),
    path("<int:pk>/upload_image/", views.AdImageUpdateView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
