import json

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models import Ad
from user.models import User
from lesson28.settings import MAX_PAGE


# Create your views here.





class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)


        user = self.object_list.order_by('first_name')
        response = []
        panginator = Paginator(user, MAX_PAGE)

        for users in user:
            ad_qs = Ad.objects.all().filter(author_id=users.id).filter(is_published=True)
            response.append({"id": users.id,
                             "username": users.username,
                             "first_name": users.first_name,
                             "last_name": users.last_name,
                             "role": users.role,
                             "age": users.age,
                             "locations": [users.location.name],
                             "total_ads": ad_qs.count()
                             })

        return JsonResponse({"items": response,
                             "total": user.count(),
                             "num_pages": panginator.num_pages})


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ad_qs = Ad.objects.all().filter(author_id=self.object.id).filter(is_published=True)

        return JsonResponse({"id": self.object.id,
                             "username": self.object.username,
                             "first_name": self.object.first_name,
                             "last_name": self.object.last_name,
                             "role": self.object.role,
                             "age": self.object.age,
                             "locations": [self.object.location.name],
                             "total_ads": ad_qs.count()
                             })


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user_create = User.objects.create(username=user_data['username'],
                                          password=user_data['password'],
                                          first_name=user_data['first_name'],
                                          last_name=user_data['last_name'],
                                          role=user_data['role'],
                                          age=user_data['age'],
                                          location_id=user_data['location_id'])
        user_create.save()

        return JsonResponse({"id": user_create.id,
                             "username": user_create.username,
                             "first_name": user_create.first_name,
                             "last_name": user_create.last_name,
                             "role": user_create.role,
                             "age": user_create.age,
                             "locations": user_create.location.name
                             })


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'age', 'location']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        self.object.username = user_data['username']
        self.object.password = user_data['password']
        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data['last_name']
        self.object.age = user_data['age']
        self.object.location_id = user_data['location_id']

        return JsonResponse({"id": self.object.id,
                             "username": self.object.username,
                             "first_name": self.object.first_name,
                             "last_name": self.object.last_name,
                             "age": 18,
                             "locations": [self.object.location.name]
                             })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"})
