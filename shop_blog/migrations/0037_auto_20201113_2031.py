# Generated by Django 3.1.2 on 2020-11-13 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0036_auto_20201113_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 20, 30, 59, 826938), verbose_name='زمان ارسال'),
        ),
    ]
