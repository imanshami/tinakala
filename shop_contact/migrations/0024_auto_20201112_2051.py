# Generated by Django 3.1.2 on 2020-11-12 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_contact', '0023_auto_20201112_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userticket',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 12, 20, 51, 32, 441424), verbose_name='زمان ایجاد تیکت'),
        ),
        migrations.AlterField(
            model_name='userticketanswer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 12, 20, 51, 32, 441424), verbose_name='زمان پاسخ تیکت'),
        ),
    ]
