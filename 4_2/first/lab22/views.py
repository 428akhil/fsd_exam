
from django.shortcuts import render 
from lab22.models import Students,Course 
from django.http import HttpResponse,HttpResponseRedirect,FileResponse 
from reportlab.pdfgen import canvas 
from django.views import generic 
 
import csv 
def download_csv(queryset): 
    opts = queryset.model._meta 
    model = queryset.model 
    response = HttpResponse(content_type='text/csv') 
    # force download. 
    response['Content-Disposition'] = 'attachment;filename=export.csv' 
    # the csv writer 
    writer = csv.writer(response) 
    field_names = [field.name for field in opts.fields] 
    # Write a first row with header information 
    writer.writerow(field_names) 
    for obj in queryset: 
        writer.writerow([getattr(obj, field) for field in field_names]) 
    return response 
 
def download(request): 
 
    data = download_csv(Course.objects.all()) 
 
    return HttpResponse (data, content_type='text/csv') 
 
def generate_pdf_file(): 
    from io import BytesIO 
 
    buffer = BytesIO() 
    p = canvas.Canvas(buffer) 
 
    # Create a PDF document 
 
    courses = Course.objects.all() 
    p.drawString(100, 750, "Course Details") 
 
    y = 700 
    for course in courses: 
        p.drawString(100, y, f"Title: {course.cname}") 
        p.drawString(100, y - 20, f"Code: {course.ccode}") 
        p.drawString(100, y - 40, f"Credits: {course.credits}") 
        y -= 60 
 
    p.showPage() 
    p.save() 
 
    buffer.seek(0) 
    return buffer 
 
def generate_pdf(request): 
    response = FileResponse(generate_pdf_file(),  
                            as_attachment=True, 
                            filename='course_details.pdf') 
    return response 

class StudentListView(generic.ListView): 
    model = Students 
    template_name = 'student_list.html'


class StudentDetailView(generic.DetailView): 
    model = Students 
    template_name = "student_detail.html" 
