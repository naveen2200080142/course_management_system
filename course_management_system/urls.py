"""course_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path("contactus/",views.contactus,name="contact"),
    path("about/",views.about,name="about"),
    path('adminapp/',include("adminapp.urls")),
    path("facultylogin/",views.facultylogin,name="facultylogin"),
    path("studentlogin/",views.studentlogin,name="studentlogin"),
    path('faculty/',include("faculty.urls"),name='faculty'),
    path('student/',include("student.urls"),name='student'),



]
