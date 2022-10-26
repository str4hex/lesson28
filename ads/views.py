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
        if ad_cat:
            try:
                self.queryset = self.queryset.filter(category=ad_cat)
            except ValueError as e:
                print(e)
            return super().list(request, *args, **kwargs)
        elif ad_text:
            try:
                self.queryset = self.queryset.filter(name__contains=ad_text)
            except ValueError as e:
                print(e)
            return super().list(request, *args, **kwargs)

        else:
            return super().list(request, *args, **kwargs)