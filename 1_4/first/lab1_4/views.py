from django.shortcuts import render 
from django.http import HttpResponse 
 
import datetime 
def current_datetime(request): 
    now=datetime.datetime.now() 
    html = "<html><body><h1>It is now %s.</h1></body></html>" % now 
    return HttpResponse(html) 
 
def four_hours_ahead(request): 
     
    dt = datetime.datetime.now() + datetime.timedelta(hours=4) 
    html = "<html><body><h1>After 4 hour(s), it will be %s.</h1></body></html>"% (dt,) 
    return HttpResponse(html) 
 
def four_hours_before(request): 
     
    dt = datetime.datetime.now() + datetime.timedelta(hours=-4) 
    html = "<html><body><h1>Before 4 hour(s), it was %s.</h1></body></html>"% (dt,) 
    return HttpResponse(html) 
 
def four_hours_ahead_dynamic(request,offset): 
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset) 
    html="<html><body><h1> After %s hours(s), It will be %s.</h1></body></html>" % (offset,dt) 
    return HttpResponse(html) 
 
def four_hours_before_dynamic(request,offset): 
    dt = datetime.datetime.now() + datetime.timedelta(hours=-offset) 
    html="<html><body><h1> before %s hours(s), It will be %s.</h1></body></html>" % (offset,dt) 
    return HttpResponse(html) 
 
# Create your views here.