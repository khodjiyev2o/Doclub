# Generated by Django 4.2.6 on 2023-12-21 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_certificate_full_name_alter_certificate_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='full_name',
        ),
    ]
