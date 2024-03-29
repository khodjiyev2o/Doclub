# Generated by Django 4.2.6 on 2023-12-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='full_name',
            field=models.CharField(default=1, max_length=255, verbose_name='Full Name of the Owner'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificate',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='certificates', verbose_name='File'),
        ),
    ]
