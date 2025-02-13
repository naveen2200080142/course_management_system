from django.shortcuts import render,HttpResponse
from student import views
def home(request):
    return render(request,'index.html')
def login (request):
    return render(request,'login.html')
def  contactus(request):
    return render(request,"contact1.html")
def about(request):
    return render(request,"about.html")
def student(request):
    return views.student


def facultylogin(request):
    return render(request,"facultylogin.html")
def studentlogin(request):
    return render(request,"studentlogin.html")
