from django.conf.urls.static import static
from django.urls import path

from user import views
from lesson28 import settings

urlpatterns = [

    path("", views.UserListView.as_view()),
    path("<int:pk>/", views.UserDetailView.as_view()),
    path("create/", views.UserCreateView.as_view()),
    path("<int:pk>/update/", views.UserUpdateView.as_view()),
    path("<int:pk>/delete/", views.UserDeleteView.as_view())


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
