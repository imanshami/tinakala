# Generated by Django 3.1.2 on 2020-11-04 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_contact', '0006_auto_20201104_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='userticket',
            name='active',
            field=models.BooleanField(default=True, verbose_name='تیکت فعال/غیرفعال'),
        ),
        migrations.AlterField(
            model_name='userticketanswer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 4, 23, 12, 33, 315888), verbose_name='زمان پاسخ تیکت'),
        ),
    ]
