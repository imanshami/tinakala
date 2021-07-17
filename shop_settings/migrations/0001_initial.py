# Generated by Django 3.1.2 on 2020-10-20 11:11

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import tinakala.utils.upload_file_manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان سایت')),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=150, size=[128, 36], upload_to=tinakala.utils.upload_file_manager.upload_site_logo, verbose_name='لوگوی سایت')),
                ('site_birth', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد سایت')),
                ('abstract', models.TextField(max_length=500, verbose_name='خلاصه معرفی')),
                ('copyright', models.CharField(max_length=100, verbose_name='متن کپی رایت')),
                ('copyright_access', models.CharField(max_length=200, verbose_name='اجازه کپی رایت مطالب')),
                ('privacy_rules', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='متن حریم خصوصی')),
                ('link_twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='لینک تویتر')),
                ('link_telegram', models.CharField(blank=True, max_length=100, null=True, verbose_name='لینک تلگرام')),
                ('link_instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='لینک اینستگرام')),
                ('link_facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='لینک فیسبوک')),
                ('samandehi', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=150, size=[145, 145], upload_to=tinakala.utils.upload_file_manager.upload_site_certificate, verbose_name='نماد سازمان ساماندهی')),
                ('link_samandehi', models.CharField(blank=True, max_length=90, null=True, verbose_name='لینک سازمان ساماندهی')),
                ('electronic', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=150, size=[145, 145], upload_to=tinakala.utils.upload_file_manager.upload_site_certificate, verbose_name='نماد سازمان تجارت الکترونیک')),
                ('link_electronic', models.CharField(blank=True, max_length=90, null=True, verbose_name='لینک سازمان تجارت الکترونیک')),
                ('sms_message', models.CharField(max_length=120, verbose_name='متن پیامک فعال سازی')),
            ],
            options={
                'verbose_name': 'تنظیمات وب اپلیکیشن',
                'verbose_name_plural': 'تنظیمات وب اپلیکیشن',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20, verbose_name='نام استان')),
            ],
            options={
                'verbose_name': 'استان',
                'verbose_name_plural': 'مدیریت استان ها',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20, verbose_name='نام شهر')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_settings.state', verbose_name='مربوط به استان')),
            ],
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'مدیریت شهرها',
            },
        ),
    ]
