# Generated by Django 3.1.2 on 2020-11-13 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_website', '0003_auto_20201113_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletters',
            options={'verbose_name': 'کاربر خبرنامه', 'verbose_name_plural': 'مدیریت کاربران خبرنامه'},
        ),
        migrations.RemoveField(
            model_name='newslettersmessage',
            name='to_users',
        ),
    ]
