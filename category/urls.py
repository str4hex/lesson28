from django.conf.urls.static import static
from django.urls import path

from category import views
from lesson28 import settings

urlpatterns = [

    path('', views.CategoryListView.as_view()),
    path("<int:pk>/", views.CategoryDetailView.as_view()),
    path("create/", views.CategoryCreateView.as_view()),
    path("<int:pk>/update/", views.CategoryUpdateView.as_view()),
    path("<int:pk>/delete/", views.CategoryDeleteView.as_view()),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
