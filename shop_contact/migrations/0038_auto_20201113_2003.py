# Generated by Django 3.1.2 on 2020-11-13 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_contact', '0037_auto_20201113_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userticket',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 20, 3, 26, 8741), verbose_name='زمان ایجاد تیکت'),
        ),
        migrations.AlterField(
            model_name='userticketanswer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 20, 3, 26, 8741), verbose_name='زمان پاسخ تیکت'),
        ),
    ]
