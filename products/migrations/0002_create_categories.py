# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 12:37
from __future__ import unicode_literals

from django.db import migrations


def migrate_categories(apps, schema_editor):
    if not schema_editor.connection.alias == 'default':
        return

    OrigCategory = apps.get_model('markets', 'ProductCategory')
    NewCategory = apps.get_model('products', 'Category')

    for category in OrigCategory.objects.all():
        new_category = NewCategory.objects.create(name=category.name)
        category.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0011_auto_20160907_1005'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_categories),
    ]