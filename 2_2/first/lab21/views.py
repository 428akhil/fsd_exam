from django.shortcuts import render 
from django.http import HttpResponse 
from django.template import loader 

def aboutus(request): 
    return render(request, 'aboutus.html') 
 
def contactus(request): 
    return render(request, 'contactus.html') 
 
def home(request): 
    return render(request, 'home.html') 