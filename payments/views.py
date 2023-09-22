import json
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from base.models import Course, UserProfile
from payments.models import Order, OrderItem, Payment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse
import datetime

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def Checkout(request, pk):
   context={}
   course = Course.objects.get(id=pk)
   context={ 'course': course }
   return render(request, 'base/checkout.html', context)

@login_required
def Pay_course(request, pk, credit_quantity, total_price):
   context={}
   course = Course.objects.get(id=pk)
   context={ 'course': course, 'credit_quantity': credit_quantity, 'total_price': total_price }
   return render(request, 'base/payment.html', context)

def charge(request):
   if request.method == 'POST':
       print('Data:', request.POST)
        
       amount = int(request.POST['amount'])

       customer = stripe.Customer.create( email=request.POST['email'], name=request.POST['name'], phone=request.POST['phone'], source=request.POST['stripeToken'] )
       charge = stripe.Charge.create( customer=customer, amount=amount*100, currency='aud', description="Course credit payment" )

       data_order = Order()
       ordercourse = OrderItem()
       data_payment = Payment()

       user_pk = request.POST['user_id']
       full_name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       order_total = '%.2f'%float(amount)
       course_id = request.POST['course_id']
       credit_quantity = request.POST['credit_quantity']
       course_price = request.POST['course_price']

       data_userprofile = UserProfile.objects.get(user_id=user_pk)

       # Store all the billing information inside Order table 
       if (user_pk and full_name  and email and phone and order_total ):
           
           # Store Payment data (stripe token)
           data_payment.user_id = user_pk
           data_payment.payment_id = request.POST['stripeToken']
           data_payment.payment_method = "Card"
           data_payment.amount_paid = amount
           data_payment.status = True
           data_payment.save()

           data_order.user_id = user_pk
           data_order.payment_id = data_payment.id
           data_order.name = full_name
           data_order.email = email
           data_order.phone = phone
           data_order.order_total = order_total
           data_order.save()

           # Generate order number
           now = datetime.datetime.now()
           current_date = now.strftime("%Y%m%d") #20230305
           order_number = current_date + str(data_order.id)
           data_order.order_number = order_number
           data_order.is_ordered = True
           data_order.save()

           

           # Store Course where credit has been purchased inside OrderItem table
           ordercourse.order_id = data_order.id
           ordercourse.payment_id = data_payment.id
           ordercourse.user_id = user_pk
           ordercourse.course_id = course_id
           ordercourse.price = course_price
           ordercourse.ordered = True
           ordercourse.save()

           # Increase user Credit
           data_userprofile.credits = int(data_userprofile.credits) + (int(credit_quantity)*60*60)
           data_userprofile.save()
   return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
   amount = args  
   return render(request, 'base/success.html', {'amount':amount})



