# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-07 14:52
from __future__ import unicode_literals

import os

from django.db import migrations
from django.core.management import call_command
from core.utils import safe_load_fixture


fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))


def load_fixture(apps, schema_editor):
    fixture_filename = 'initial_0004.json'
    fixture_path = os.path.join(fixture_dir, fixture_filename)
    safe_load_fixture(apps, fixture_path)


def unload_fixture(apps, schema_editor):
    call_command('flush', interactive=False)
    fixture_filename = 'initial_0003.json'
    fixture_path = os.path.join(fixture_dir, fixture_filename)
    safe_load_fixture(apps, fixture_path)


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20161103_1038'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
