# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lane_miles', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='RouteSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highway', models.CharField(max_length=200)),
                ('segment_name', models.CharField(max_length=200)),
                ('ring', models.IntegerField(default=1)),
                ('length', models.DecimalField(default=0, max_digits=5, blank=True, decimal_places=2)),
                ('lanes', models.IntegerField(default=10)),
                ('lane_miles', models.DecimalField(default=0, max_digits=5, blank=True, decimal_places=2)),
                ('start_lat', models.DecimalField(max_digits=10, decimal_places=6)),
                ('start_lng', models.DecimalField(max_digits=10, decimal_places=6)),
                ('end_lat', models.DecimalField(max_digits=10, decimal_places=6)),
                ('end_lng', models.DecimalField(max_digits=10, decimal_places=6)),
                ('geojson', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
