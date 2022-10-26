from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers

from user import views
from lesson28 import settings
from user.views import LocationViewList

router = routers.SimpleRouter()
router.register('location', LocationViewList)


urlpatterns = [


    path("", views.UserListView.as_view()),
    path("user/<int:pk>/", views.UserDetailView.as_view()),
    path("user/create/", views.UserCreateView.as_view()),
    path("user/<int:pk>/update/", views.UserUpdateView.as_view()),
    path("user/<int:pk>/delete/", views.UserDeleteView.as_view())


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls