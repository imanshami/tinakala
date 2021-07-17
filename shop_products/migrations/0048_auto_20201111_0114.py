# Generated by Django 3.1.2 on 2020-11-10 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0047_auto_20201111_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_visited',
            field=models.PositiveIntegerField(default=1, verbose_name='بازدید کل'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 1, 14, 27, 771489), verbose_name='زمان ارسال'),
        ),
    ]
