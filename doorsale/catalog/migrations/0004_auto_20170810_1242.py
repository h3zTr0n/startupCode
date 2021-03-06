# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-10 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170810_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='location_name',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='cell',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='province_name',
        ),
        migrations.AddField(
            model_name='product',
            name='cell',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='product',
            name='location_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='product',
            name='province_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Location'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_free_shipping',
            field=models.BooleanField(default=False, help_text='No Delivery charges'),
        ),
    ]
