# Generated by Django 3.1.2 on 2020-11-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_order', '0002_order_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_code',
            field=models.CharField(max_length=12, null=True, verbose_name='کد سفارش'),
        ),
    ]
