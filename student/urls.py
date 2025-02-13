from django.urls import path
from . import views

urlpatterns = [
    path('',views.studenthome,name="studenthome"),
    path("student/", views.student, name="studentlogin"),
    path("checkstudentlogin",views.checkstudentlogin,name="checkstudentlogin"),
    path("studentcourses",views.studentcourses,name="studentcourses"),
    path("studentchangepwd",views.studentchangepwd,name="studentchangepwd"),
    path("studentchangepwd",views.studentupdatepwd,name="studentupdatepwd"),
    path("displaystudentcourses",views.dispalystudentcourses,name="displaystudentcourses"),

]