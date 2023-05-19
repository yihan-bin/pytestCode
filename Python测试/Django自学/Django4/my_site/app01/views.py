import datetime

from django.shortcuts import render,HttpResponse,\
from django.views.decorators.csrf import csrf_exempt
import pymysql
import os
# Create your views here.
def current_datatime(reqeset):
    now=datetime.datetime.now()
    html='<html><bode> It is now %s.</body></html>' %now
    print(HttpResponse.scheme)
    print(HttpResponse.path)
    print(HttpResponse.scheme)
    return HttpResponse(html)
@csrf_exempt
def index(request):
    print(request.content_type)
    print(request.GET,request.POST)
  #  print(request.POST.get('f_test'))
    print(request.FILES)
    return render(request,'form.html')


