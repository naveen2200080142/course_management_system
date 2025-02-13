
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin,name="adminlogin"),
    path("home/", views.adminhome,name="adminhome"),
    path('chechadminlogin/',views.checkadminlogin,name="checkadminlogin"),
    path("adminchangepwd/", views.adminchangepwd,name="adminchangepwd"),
    path("adminstudent/", views.adminstudent,name="adminstudent"),
    path("adminfaculty/", views.adminfaculty,name="adminfaculty"),
    path("admincourse/", views.admincourse,name="admincourse"),
    path("adminupdatepass",views.adminupdatepwd,name="adminupdatepwd"),
    path("facultycoursemapping",views.facultycoursemapping,name="facultycoursemapping"),
    path("viewcourses/",views.viewcourses,name="viewcourses"),
    path("viewfaculty/",views.viewfaculty,name="viewfaculty"),
    path("viewstudents/",views.viewstudents,name="viewstudents"),
    path("addcourse",views.addcourse,name="addcourse"),
    path("deletecourse",views.deletecourse,name="deletecourse"),
    path("insertcourse",views.insertcourse,name="insertcourse"),
    path("coursedeletion/<int:cid>",views.coursedeletion,name="coursedeletion/"),
    path("deletestudent", views.deletestudent, name="deletestudent"),
    path("addstudent", views.addstudent, name="addstudent"),
    path("studentdeletion/<int:cid>", views.studentdeletion, name="studentdeletion/"),
    path("deletefaculty", views.deletefaculty, name="deletefaculty"),
    path("addfaculty", views.addfaculty, name="addfaculty"),
    path("facultydeletion/<int:cid>", views.facultydeletion, name="facultydeletion/"),


]