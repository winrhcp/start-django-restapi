from django.shortcuts import render

from rest_framework import viewsets
from .serializers import RapperSerializer
from .serializers import StockSerializer
from .models import Rapper
from .models import Stock
# Create your views here.
class RapperViewSet(viewsets.ModelViewSet):
    queryset = Rapper.objects.all().order_by('aka')
    serializer_class = RapperSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('name')
    serializer_class = StockSerializer