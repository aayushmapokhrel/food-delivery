from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    class Paymentmethod(models.IntegerChoices):
        credit_card = 1, 'CREDIT CARD'
        fonepay = 2, 'FONEPAY'
        cash = 3, 'CASH'
        other = 4, 'OTHER'
    class Paymentstatus(models.IntegerChoices):
        complete = 1, 'COMPLETE'
        pending = 2, 'PENDING'
        cancelled = 3, 'CANCELLED'
        failed = 4, 'FAILED'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='payments'
        )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='NPR')
    payment_method = models.IntegerField(
        choices=Paymentmethod.choices,
        default='cash'
        )
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.IntegerField(
        choices=Paymentstatus.choices,
        default='complete'
        )

    def __str__(self):
        return f'{self.user.username} - {self.transaction_id} - {self.amount}'