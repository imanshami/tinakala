# Generated by Django 3.1.2 on 2020-11-09 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_blog', '0007_auto_20201109_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 9, 13, 56, 25, 258315), verbose_name='زمان ارسال'),
        ),
    ]
