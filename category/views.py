import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, ListView, DetailView, DeleteView, CreateView

from category.models import Category
# Create your views here.

class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        category = self.object_list.order_by('name')
        response = []

        for categorys in category:
            response.append({
                "id": categorys.id,
                "name": categorys.name
            })

        return JsonResponse(response, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse({"id": self.object.id,
                             "name": self.object.name})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category = Category.objects.create(name=category_data['name'])

        return JsonResponse({"id": category.id,
                             "name": category.name})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)
        self.object.name = category_data['name']
        self.object.save()
        return JsonResponse({"id": self.object.id,
                             "name": self.object.name})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"})
