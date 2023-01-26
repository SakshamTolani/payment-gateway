from django.urls import path
from . import views

urlpatterns = [
    path('', views.getOrders, name="get-orders"),
    path('createOrder/',views.createOrder, name="create-order"),
    path('<str:pk>/',views.getOrderById, name="get-order"),
    path('<str:pk>/paymentStatus/', views.getPaymentDetails, name='get-payment-status'),
    path('<str:pk>/paymentStatus/success/', views.paymentSuccess, name='payment-success'),
    path('<str:pk>/paymentStatus/failure/', views.paymentFailure, name='payment-failure'),
]