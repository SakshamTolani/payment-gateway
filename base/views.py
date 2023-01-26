from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.serializers import OrderSerializer, OrderCreateSerializer, PaymentDetailsSerializer
from rest_framework.reverse import reverse
from base.models import *

@api_view(['GET'])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOrderById(request,pk):
    try:
        order = Order.objects.get(order_id=pk)
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
    except:
        return Response({'detail': 'Order does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createOrder(request):
    data = request.data
    order_id = data['order_id']
    order_amount = data['order_amount']
    customer_name = data['customer_name']
    payment_url="http://localhost:8000/"+order_id+"/"
    payment_success_url="http://localhost:8000/api/"+order_id+"/paymentStatus/success/"
    payment__failure_url="http://localhost:8000/api/"+order_id+"/paymentStatus/failure/"
    order = Order.objects.create(
        order_id=order_id,
        order_amount=order_amount,
        customer_name=customer_name,
        payment_url=payment_url,
        payment_success_url=payment_success_url,
        payment_failure_url=payment__failure_url
    )
    serializer = OrderCreateSerializer(order, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPaymentDetails(request, pk):
    try:
        order = Order.objects.get(order_id=pk)
        serializer = PaymentDetailsSerializer(order, many=False)
        return Response(serializer.data)
    except:
        return Response({'detail': 'Order does not exist.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def paymentSuccess(request,pk):
    try:
        order = Order.objects.get(order_id=pk)
        order.payment_status = 'Success'
        order.save()
        serializer = PaymentDetailsSerializer(order, many=False)
        return Response({
            'message':'PAYMENT SUCCESSFUL',
            'redirect_url':reverse('get-payment-status',args=[order.order_id], request=request)
        })
    except Exception as e:
        return Response({'detail': 'Some error occured'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def paymentFailure(request,pk):
    try:
        order = Order.objects.get(order_id=pk)
        order.payment_status = 'Failure'
        order.save()
        serializer = PaymentDetailsSerializer(order, many=False)
        return Response({
            'message':'PAYMENT FAILED',
            'redirect_url':reverse('get-payment-status',args=[order.order_id], request=request)
        })
    except:
        return Response({'detail': 'Some error occured'}, status=status.HTTP_400_BAD_REQUEST)
    
