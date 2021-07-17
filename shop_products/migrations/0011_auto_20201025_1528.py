# Generated by Django 3.1.2 on 2020-10-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0010_productgallery_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'عکس (png, jpg, ...)'), (2, 'ویدیو (mp4, ...)')], null=True, verbose_name='نوع رسانه'),
        ),
    ]
