from rest_framework import serializers
from .models import GoogleSheetTable

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleSheetTable
        fields = ('order_number','order_cost_in_dollars','delivery_time','order_cost_in_rubles')