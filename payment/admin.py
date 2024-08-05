from django.contrib import admin
from payment.models import Payment


# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["amount", "currency", "payment_method", "payment_date", "transaction_id","status"]
    # search_fields = ["order"]
