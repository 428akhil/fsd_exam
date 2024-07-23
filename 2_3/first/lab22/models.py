from django.db import models 
 
# Create your models here. 
class Course(models.Model): 
    cname = models.CharField(max_length=10) 
    ccode = models.CharField(max_length=30) 
    credits = models.IntegerField() 
    def __str__(self): 
        return self.cname 
class Students(models.Model): 
    name = models.CharField(max_length=30) 
    usn = models.CharField(max_length=50) 
    sem = models.IntegerField() 
    branch = models.CharField(max_length=30) 
    sce = models.ManyToManyField(Course) 
    def __str__(self): 
        return self.name 