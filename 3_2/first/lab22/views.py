from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect,FileResponse 
from lab22.models import ProjectReg 
 
def add_project(request): 
     submitted = False 
     if request.method == 'POST': 
         form = ProjectReg(request.POST) 
         if form.is_valid(): 
             form.save() 
             return HttpResponseRedirect('/add_project/?submitted=True') 
     else: 
         form = ProjectReg() 
         if 'submitted' in request.GET: 
             submitted = True 
     return render(request, 'project_reg.html', {'form': form, 'submitted': 
submitted}) 