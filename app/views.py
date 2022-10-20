from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Ad, Category, Location, User


# Create your views here.


class AdsViewList(ListView):
    model = Ad

    def get(self, request, *args, **keargs):
        super().get(request, *args, **keargs)
        ad = self.object_list
        response = []

        for ads in ad:
            response.append({
                "Id": ads.Id,
                "name": ads.name,
                "author_id": ads.author_id,
                "price": ads.price,
                "description": ads.description,
                "is_published": ads.is_published,
                "image": ads.image.url,
                "category_id": ads.category_id
            })

        return JsonResponse(response, safe=False)


class AdsDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse({
            "Id": self.object.Id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url,
            "category_id": self.object.category_id
        })


