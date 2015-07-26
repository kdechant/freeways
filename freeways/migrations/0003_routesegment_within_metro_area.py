# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freeways', '0002_auto_20150621_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='routesegment',
            name='within_metro_area',
            field=models.BooleanField(default=1),
        ),
    ]
