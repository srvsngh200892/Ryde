# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0004_auto_20141221_1349'),
    ]

    operations = [
       migrations.AlterField(
            model_name='driver',
            name='date_left',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 55, 23, 464854)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rides',
            name='time_ended',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 55, 23, 466188)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rides',
            name='time_started',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 55, 23, 466107)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='joined',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 55, 23, 463486), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 55, 23, 463533), auto_now=True),
            preserve_default=True,
        ),
    ]
