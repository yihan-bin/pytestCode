from django.shortcuts import render,HttpResponse
import os
# Create your views here.
def test_view(reqeset):
    print('执行业务逻辑')
    print(requset)
    return HttpResponse('500一次')
def login_view(request):
    return render(request,'form.html')

#print(os.path.join(BA,"html"))
def article(request):
    return HttpResponse('article_2003')
def article_2003(request,year):
    return HttpResponse('article_时间'+year)
def article_year_month( request , arg1, arg2):
    return HttpResponse('article_时间' + arg1)

def article3(request,year,month,slug):
    return HttpResponse('article_时间' +slug)
def book_2003(request):
    return HttpResponse('book')
def book2(request,year):
    return HttpResponse('article %s'%year)
def book3(request,year,month):
    return HttpResponse('article  %s' %month)
def book4(request,year,month,slug):
    return HttpResponse('article_2003'+slug)
def book5(request,month,name):
    return HttpResponse('article_2004'+name)
def book6(request,year,name):
    return HttpResponse('article_字写url转换器'+name)