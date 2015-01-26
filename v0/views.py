from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from models import *
from django.utils import timezone
from django.db import connection
# Create your views here.
def home(request):
	get_ride_link = '<h1><a href="book">Get me a ride</a></h1>'
	context = {
		'link' : get_ride_link,
	}
	#return HttpResponse(template.render(context))	
	return render(request, 'v0/home.html', context)

def book(request):
	start_ride = Rides(last_started, long_started, time_started = timezone.now())


'''
@param current corrds, destination
@return matching rides
'''
def getLocation(request):
	#check validity of coords
	#log action
	#get nearby taxis
	rides = getNearbyRides(request['lat'], request['long'])
	if len(rides) > 0:
	data = { 'rides' : rides }
	return render( request, 'rides', data)
	
def getNearbyRides(lat, lng):
	#v1 go with SQL
	query = "SELECT * FROM ride_locations WHERE "
	cursor = connection.cursor()
	result = cursor.execute(query)



	 		
