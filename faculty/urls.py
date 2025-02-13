from django.urls import path
from . import views

urlpatterns = [
    path('faculty/',views.facultyhome,name="facultyhome"),
    path("", views.facultylogin, name="facultylogin"),
    path("checkfacultylogin",views.checkfacultylogin,name="checkfacultylogin"),
    path("Ffacultycourses/",views.Ffacultycourses,name="Ffacultycourses"),
    path("facultychangepwd/",views.facultychangepwd,name="facultychangepwd"),
    path("facultyupdatepwd",views.facultyupdatepwd,name="facultyupdatedpwd"),
]