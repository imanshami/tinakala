# Generated by Django 3.1.2 on 2020-10-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_categories', '0007_auto_20201023_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoryparent',
            name='sub_category',
            field=models.ManyToManyField(blank=True, related_name='sub_category', to='shop_categories.Category', verbose_name='دسته فرزند'),
        ),
    ]
