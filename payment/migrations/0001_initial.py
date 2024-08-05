# Generated by Django 5.0.7 on 2024-08-04 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='NPR', max_length=3)),
                ('payment_method', models.IntegerField(choices=[(1, 'CREDIT CARD'), (2, 'FONEPAY'), (3, 'CASH'), (4, 'OTHER')], default='cash')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('status', models.IntegerField(choices=[(1, 'COMPLETE'), (2, 'PENDING'), (3, 'CANCELLED'), (4, 'FAILED')], default='complete')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]