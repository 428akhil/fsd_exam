"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path 
from lab1_4.views import current_datetime, four_hours_ahead, four_hours_before, four_hours_ahead_dynamic,four_hours_before_dynamic 
 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('cdt/', current_datetime), 
    path('fhrsa/',four_hours_ahead), 
    path('fhrsb/',four_hours_before), 
    path('fhrsad/<int:offset>/',four_hours_ahead_dynamic), 
    path('fhrsbd/<int:offset>/',four_hours_before_dynamic), 
     
    
] 