# myapi/serializers.py
from rest_framework import serializers
from .models import Rapper
from .models import Stock
class RapperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rapper
        fields = ('name', 'aka')

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ('name', 'price')