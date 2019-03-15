from django.shortcuts import render
from django.http import HttpResponse
  #from college.templates import college # Create your views here.  


def index(request): 	
	return HttpResponse('Hello')