from rest_framework.viewsets import ModelViewSet
from ads.models import Ad, Category
from ads.serializer import AdsSerializer


class AdsViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer

    def list(self, request, *args, **kwargs):
        print(request.GET.get('text', None))
        ad_cat = request.GET.get('cat')
        ad_text = request.GET.get('text')
        ad_location = request.GET.get('location')
        ad_price_from = request.GET.get('price_from')
        ad_price_to = request.GET.get('price_to')

        if ad_cat:
            try:
                self.queryset = self.queryset.filter(category=ad_cat)
            except ValueError as e:
                print(e)
            return super().list(request, *args, **kwargs)
        elif ad_text:
            try:
                self.queryset = self.queryset.filter(name__icontains=ad_text)
            except ValueError as e:
                print(e)
            return super().list(request, *args, **kwargs)

        elif ad_location:
            try:
                self.queryset = self.queryset.filter(author__location__name__icontains=ad_location)
            except ValueError as e:
                print(e)
            return super().list(request, *args, **kwargs)

        elif ad_price_from and ad_price_to:
            print(ad_price_from)
            print(ad_price_to)
            try:
                self.queryset = self.queryset.filter(price__gte=ad_price_from, price__lte=ad_price_to)
            except ValueError as e:
                print(e)
            return super().list(request, *args, **kwargs)
        else:
            return super().list(request, *args, **kwargs)