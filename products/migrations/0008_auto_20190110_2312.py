# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-11 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=140),
        ),
    ]
