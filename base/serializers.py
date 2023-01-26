from rest_framework import serializers
from base.models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id','order_amount','payment_url','payment_success_url','payment_failure_url']

class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id','payment_status']
