# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freeways', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routesegment',
            name='ring',
        ),
        migrations.AddField(
            model_name='routesegment',
            name='distance_from_origin',
            field=models.DecimalField(editable=False, default=0, max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='routesegment',
            name='geojson',
            field=models.TextField(editable=False, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='routesegment',
            name='lane_miles',
            field=models.DecimalField(editable=False, default=0, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='routesegment',
            name='length',
            field=models.DecimalField(editable=False, default=0, max_digits=5, decimal_places=2),
        ),
    ]
