# Generated by Django 3.1.2 on 2020-11-04 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_contact', '0005_auto_20201103_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userticketanswer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 4, 23, 2, 48, 13751), verbose_name='زمان پاسخ تیکت'),
        ),
    ]
