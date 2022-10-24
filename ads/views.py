import json

from django.core.paginator import Paginator
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, ListView, DetailView, DeleteView, CreateView

from ads.models import Ad
from lesson28.settings import MAX_PAGE


# Create your views here.
class AdsViewList(ListView):
    model = Ad

    def get(self, request, *args, **keargs):
        super().get(request, *args, **keargs)
        ad_qs = Ad.objects.annotate(obj_name=Count('name'))
        ad = self.object_list.order_by('-price')
        response = []
        paginator = Paginator(self.object_list, MAX_PAGE)

        for ads in ad:
            response.append({"Id": ads.Id,
                             "name": ads.name,
                             "author_id": ads.author_id,
                             "author": ads.author.first_name,
                             "price": ads.price,
                             "description": ads.description,
                             "is_published": ads.is_published,
                             "image": ads.image.url if ads.image else None,
                             "category": ads.category.name
                             })

        return JsonResponse({"items": response,
                             "total": ad.count(),
                             "num_pages": paginator.num_pages,
                             "avg": ad_qs.aggregate(Avg('Id'))
                             })


class AdsDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse({"Id": self.object.Id,
                             "name": self.object.name,
                             "author_id": self.object.author_id,
                             "author": self.object.author.first_name,
                             "price": self.object.price,
                             "description": self.object.description,
                             "is_published": self.object.is_published,
                             "image": self.object.image.url if self.object.image else None,
                             "category": self.object.category.name
                             })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(name=ad_data['name'],
                               author_id=ad_data['author_id'],
                               price=ad_data['price'],
                               description=ad_data['description'],
                               is_published=ad_data['is_published'],
                               category_id=ad_data['category_id']
                               )

        return JsonResponse({"id": ad.Id,
                             "name": ad.name,
                             "author_id": ad.author_id,
                             "author": ad.author.first_name,
                             "price": ad.price,
                             "description": ad.description,
                             "is_published": ad.is_published,
                             "category": ad.category.name,
                             "image": ad.image.url if ad.image else None
                             })


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'category']

    def patch(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        ad = self.object
        ad.name = ad_data['name']
        ad.author_id = ad_data['author_id']
        ad.price = ad_data['price']
        ad.description = ad_data['description']
        ad.category_id = ad_data['category_id']

        return JsonResponse({"id": ad.Id,
                             "name": ad.name,
                             "author_id": ad.author_id,
                             "author": ad.author.first_name,
                             "price": ad.price,
                             "description": ad.description,
                             "is_published": ad.is_published,
                             "category": ad.category.name,
                             "image": ad.image.url if ad.image else None
                             })


@method_decorator(csrf_exempt, name='dispatch')
class AdImageUpdateView(UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        try:

            self.object.image = request.FILES['image']

        except:
            self.object.image = None

        self.object.save()

        return JsonResponse({"id": self.object.Id,
                             "name": self.object.name,
                             "author_id": self.object.author_id,
                             "author": self.object.author.first_name,
                             "price": self.object.price,
                             "description": self.object.description,
                             "is_published": self.object.is_published,
                             "category": self.object.category.name,
                             "image": self.object.image.url if self.object.image else None
                             })
