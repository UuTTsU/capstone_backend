from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
from .models import Wiwako
from config.carousel.models import CarouselItem
from .serializers import WiwakoSerializer, CarouselItemSerializer
from django.db.models import Q
from rest_framework.generics import RetrieveAPIView
# from rest_framework.views import APIView







class Pagination(PageNumberPagination):
     page_size = 3
     page_size_query_param = 'page_size'
     max_page_size = 1000


class HomeAPIView(ListAPIView):
    queryset = Wiwako.objects.all()[:3]
    serializer_class = WiwakoSerializer

class CarouselApi(ListAPIView):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer

class WiwakoDetailAPIView(RetrieveAPIView):
    queryset = Wiwako.objects.all()
    serializer_class = WiwakoSerializer
    lookup_field = 'id'


class ProductPageAPIView(ListAPIView):
    serializer_class = WiwakoSerializer
    pagination_class = Pagination

    def get_queryset(self):
        category_name = self.request.GET.get('category')
        price_range = self.request.GET.get("price")
        queryset = Wiwako.objects.all().order_by("-id")
        
        if category_name:
            queryset = queryset.filter(category__name=category_name)
        
        if price_range:
            min_price, max_price = map(float, price_range.split('-'))
            queryset = queryset.filter(fasi__gte=min_price, fasi__lte=max_price).order_by("-fasi")
        
        return queryset

class SearchResultsAPIView(ListAPIView):
     serializer_class = WiwakoSerializer
     pagination_class = Pagination

     def get_queryset(self):
         query = self.request.GET.get('query')
         queryset = Wiwako.objects.all().order_by("-id")
        
         if query:
            queryset = queryset.filter(
                 Q(saxeli_qartulad__icontains=query) | Q(saxeli_inglisurad__icontains=query)
             )
        
         return queryset