# Generated by Django 3.1.2 on 2020-11-09 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0040_auto_20201109_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 9, 21, 22, 47, 441149), verbose_name='زمان ارسال'),
        ),
    ]
