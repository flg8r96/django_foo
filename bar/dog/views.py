from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from urlparse import parse_qsl
from dog.models import datasink

@csrf_exempt
def index(request):
	if request.method == 'GET':
		return HttpResponse("GET")
	elif request.method == 'POST':
		print "body: " +request.body
		print "body_qsl: " +str(parse_qsl(request.body))
		dbread1 = datasink.objects.all()
		print "DB Before POST: " +str(dbread1)
		dbwrite = datasink(str(parse_qsl(request.body)))
		#dbwrite.save()
		#dbread2 = datasink.ojects.all()
		print "DB After POST: " +str(output)
		return HttpResponse("POST " +str(parse_qsl(request.body)))
	else:
		return HttpResponse("Neither POST or GET")
