# Generated by Django 3.1.2 on 2020-10-30 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_categories', '0009_brands'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='en_title',
            field=models.CharField(default='', max_length=120, verbose_name='عنوان انگلیسی برند'),
            preserve_default=False,
        ),
    ]
