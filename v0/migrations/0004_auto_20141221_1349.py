# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0003_auto_20141221_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rides_log',
            old_name='driver_id',
            new_name='driver',
        ),
        migrations.RenameField(
            model_name='rides_log',
            old_name='ride_id',
            new_name='ride',
        ),
        migrations.RenameField(
            model_name='rides_log',
            old_name='rider_id',
            new_name='rider',
        ),
        migrations.AlterField(
            model_name='driver',
            name='date_left',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 49, 22, 366703)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rides',
            name='time_ended',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 49, 22, 369921)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rides',
            name='time_started',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 49, 22, 369820)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='joined',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 49, 22, 363558), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 49, 22, 363700), auto_now=True),
            preserve_default=True,
        ),
    ]
