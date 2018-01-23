from django.shortcuts import render

import json
# Create your views here.
from django.http import HttpResponse
from weixin.models import Toutiao
from datetime import datetime
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


def index(request):
    data = Toutiao.objects.all().values()
    datas = list(data)
    return HttpResponse(json.dumps(datas), content_type="application/json")
   # return HttpResponse("Hello, world. You're at the polls index."+ {'author_list' : a})


def add(request):
    path = r"students_toutiao.json"
    file = open(path, "rb")
    fileJson = json.load(file)
    alldata=fileJson['RECORDS']
    for i in alldata:
        print(i)
        Toutiao.objects.create(i)
    return HttpResponse(json.dumps(alldata), content_type="application/json")
