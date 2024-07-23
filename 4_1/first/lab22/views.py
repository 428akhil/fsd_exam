
from django.shortcuts import render 
from lab22.models import Students,Course 
from django.http import HttpResponse 
from django.http import HttpResponse,HttpResponseRedirect,FileResponse 
from lab22.models import ProjectReg 
from django.views import generic 
 
class StudentListView(generic.ListView): 
    model = Students 
    template_name = 'student_list.html' 
 
class StudentDetailView(generic.DetailView): 
    model = Students 
    template_name = "student_detail.html" 