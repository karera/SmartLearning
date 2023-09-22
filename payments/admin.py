from django.contrib import admin
from payments.models import Payment, Order, OrderItem
from django.utils.html import format_html

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('image_tag','course',
    'price', 'payment', 'ordered','user')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'order_total', 'is_ordered', 'created_at']
    list_filter = ['order_total', 'is_ordered','user',]
    list_per_page = 50
    inlines = [OrderItemInline]

class OrderItemAdmin(admin.ModelAdmin):
    def course_thumbnail(self, object):
        try:
            return format_html('<img src="{}" width="80" style="border-radius:10%;border:1px solid #000">'.format(object.course.thumbnail.url))
        except:
            return ""
    course_thumbnail.short_description = 'Product Picture'

    list_display = ['course_thumbnail', 'user', 'ordered', 'price', 'course']
    list_display_links = ("course_thumbnail", "course",)
    list_filter = ['ordered', 'user',]
    list_per_page = 50

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)