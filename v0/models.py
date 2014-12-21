from django.db import models
from datetime import datetime


class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	username = models.SlugField(max_length=10, default = '')
	# password = models.
	joined = models.DateField(auto_now_add=True, default=datetime.now())
	last_updated = models.DateField(auto_now=True, default=datetime.now())	
	phone_number = models.CharField(max_length=15, default = '')
	
class Rides_log(models.Model):
	driver = models.ForeignKey('Driver')
	rider = models.ForeignKey('Rider')
	ride = models.ForeignKey('Rides')

class Driver(User):
	date_left = models.DateField(auto_now=False, default=datetime.now())
	
class Rider(User):
	level = models.IntegerField()

class Rides(models.Model):
	time_started = models.DateField(auto_now=False, default=datetime.now())
	time_ended = models.DateField(auto_now=False, default=datetime.now())
	lat_started = models.CharField(max_length=50)
	long_started = models.CharField(max_length=50)
	lat_ended = models.CharField(max_length=50)
	long_ended = models.CharField(max_length=50)
			
