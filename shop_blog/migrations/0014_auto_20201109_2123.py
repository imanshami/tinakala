# Generated by Django 3.1.2 on 2020-11-09 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0013_auto_20201109_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 9, 21, 23, 17, 193099), verbose_name='زمان ارسال'),
        ),
    ]
