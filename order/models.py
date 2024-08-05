from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth.models import User


class Order(models.Model):
    class Orderstatus(models.IntegerChoices):
        pending = 1, 'Pending'
        preparing = 2, 'Preparing'
        out_for_delivery = 3, 'Out for Delivery'
        delivered = 4, 'Delivered'
        cancelled = 5, 'Cancelled'

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(
        choices=Orderstatus.choices,
        default='pending'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.customer


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
        )
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)