from django.contrib import admin
from order.models import Order, OrderItem


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["restaurant", "created_at", "status"]
    search_fields = ["restaurant"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["item_name", "quantity", "price_per_unit"]
    # search_fields=['driver']
