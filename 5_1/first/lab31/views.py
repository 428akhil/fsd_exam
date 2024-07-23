from django.shortcuts import render 
from lab22.models import Students,Course 
from django.http import HttpResponse 
 
# Create your views here. 
def registerAJ(request): 
    if request.method == 'POST': 
        sname = request.POST.get('sname') 
        cname = request.POST.get('cname') 
        students = Students.objects.filter(name=sname).values() 
        if students: 
            print(students.first()) 
            sid=students.first()['id'] 
            s=Students.objects.get(id=sid) 
            courses = Course.objects.filter(cname=cname).values() 
            if courses: 
                cid=courses.first()['id'] 
                c=Course.objects.get(id=cid) 
                s.sce.add(c) 
                return render(request,'registerAJ.html', {'message': 'Successfully registered'}) 
            else: 
                return render(request,'registerAJ.html',{'message': 'Course not found'}) 
        else: 
            return render(request,'registerAJ.html',{'message': 'Student not found'}) 
    else: 
        return render(request,'sentryAJ.html')