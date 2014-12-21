# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='v0.User')),
                ('date_left', models.DateField(default=datetime.datetime(2014, 12, 21, 13, 46, 26, 761627))),
            ],
            options={
            },
            bases=('v0.user',),
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='v0.User')),
                ('level', models.IntegerField()),
            ],
            options={
            },
            bases=('v0.user',),
        ),
        migrations.CreateModel(
            name='Rides',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_started', models.DateField(default=datetime.datetime(2014, 12, 21, 13, 46, 26, 762857))),
                ('time_ended', models.DateField(default=datetime.datetime(2014, 12, 21, 13, 46, 26, 762896))),
                ('lat_started', models.CharField(max_length=50)),
                ('long_started', models.CharField(max_length=50)),
                ('lat_ended', models.CharField(max_length=50)),
                ('long_ended', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rides_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('driver_id', models.ForeignKey(to='v0.Driver')),
                ('ride_id', models.ForeignKey(to='v0.Rides')),
                ('rider_id', models.ForeignKey(to='v0.Rider')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='joined',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 46, 26, 760306), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2014, 12, 21, 13, 46, 26, 760350), auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=b'', max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.SlugField(default=b'', max_length=10),
            preserve_default=True,
        ),
    ]
