# Generated by Django 3.1 on 2020-09-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200913_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgjobpost',
            name='Job_Site_Address',
            field=models.CharField(default='India', max_length=60),
        ),
    ]
