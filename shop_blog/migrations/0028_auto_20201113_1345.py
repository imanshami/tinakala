# Generated by Django 3.1.2 on 2020-11-13 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0027_auto_20201113_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 13, 45, 1, 921260), verbose_name='زمان ارسال'),
        ),
    ]
