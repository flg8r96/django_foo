from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from urlparse import parse_qsl, parse_qs
from dog.models import datasink
import json


@csrf_exempt
def index(request):
    encoding = 1    # 0 = urlencode, 1 = json

    if request.method == 'GET':
        print "\nThis is a " + request.method
        return HttpResponse("GET - oh yeah")
    elif request.method == 'POST':
        print "\nThis is a " + request.method
        print "body: " + request.body

        if encoding:
            parsed = json.loads(request.body)
        else:
            parsed = parse_qsl(request.body)

        dict_parse = dict(parsed)
        print "str_parsed .. body_qsl: " + str(parsed)
        print dict_parse
        dbread1 = datasink.objects.all()
        print "DB Before POST: " + str(dbread1)
        datasink.objects.create(**dict_parse)
        print dbread1.__len__()
        print dbread1.order_by()
        return HttpResponse("POST")
    else:
        return HttpResponse("Neither POST or GET")
