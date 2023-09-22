from django.db import models
from custom_accounts.models import User
from base.models import Course
from django.utils.html import format_html
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100) # this is the total amount paid
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    payment_mode = models.CharField(max_length=200, default='Stripe')
    order_number = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=50)
    order_total = models.FloatField(max_length=200)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.name
    
    @property
    def image_tag(self):
        var_image = self.course.thumbnail.url
        return format_html('<img src="{0}" width="80" height="80" style="border-radius:5px;border:1px solid #000">'.format(var_image))