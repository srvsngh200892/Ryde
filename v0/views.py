from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.
def home(request):
	return HttpResponse('<h1>ok!</h1')
