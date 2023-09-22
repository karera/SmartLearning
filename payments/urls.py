from django.urls import path
from payments import views

urlpatterns = [
    path('checkout/<int:pk>/', views.Checkout, name='checkout'),
    path('pay_course/<int:pk>/<int:credit_quantity>/<int:total_price>/', views.Pay_course, name='pay_course'),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
]