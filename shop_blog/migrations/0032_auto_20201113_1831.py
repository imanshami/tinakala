# Generated by Django 3.1.2 on 2020-11-13 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0031_auto_20201113_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 18, 31, 42, 72409), verbose_name='زمان ارسال'),
        ),
    ]
