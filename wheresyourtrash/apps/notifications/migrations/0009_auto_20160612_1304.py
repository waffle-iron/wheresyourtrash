# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_auto_20160611_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressblock',
            name='name',
        ),
        migrations.RemoveField(
            model_name='addressblock',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='addressblock',
            name='trashed',
        ),
        migrations.AlterField(
            model_name='municipality',
            name='districts_map',
            field=models.ImageField(blank=True, null=True, upload_to='notifications/maps/', verbose_name='Districts Map'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscription_type',
            field=models.CharField(choices=[('SMS', 'Text message'), ('EMAIL', 'Email')], max_length=20, verbose_name='Type'),
        ),
    ]
