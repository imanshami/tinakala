# Generated by Django 3.1.2 on 2020-10-27 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_products', '0024_auto_20201027_2108'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop_accounts', '0005_auto_20201027_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCommentVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(choices=[(True, 'می پسندم'), (False, 'نمی پسندم')], verbose_name='امتیاز شما')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت امتیاز')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_products.productcomment', verbose_name='مربوط به کامنت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر ارسال کننده')),
            ],
            options={
                'verbose_name': 'امتیاز نظر',
                'verbose_name_plural': 'مدیریت امتیاز نظرات',
            },
        ),
    ]
