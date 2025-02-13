from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from adminapp.models import Admin,Course,Student,Faculty
# Create your views here.
def studenthome(request):
    sid = request.session["sid"]
    print(sid)


    return render(request, "studenthome.html", {"sid": sid})

def student(request):
    return render(request,"studentlogin.html")
def checkstudentlogin(request):

    sid=request.POST["sid"]
    adminpass = request.POST["pwd"]
    flag=Student.objects.filter(Q(studentid=sid)&Q(password=adminpass))
    if flag:

        request.session["sid"] = sid
        student = Student.objects.get(studentid=sid)
        return render(request,'studenthome.html',{"sid":sid,"student":student})
    else:
        return HttpResponse("login failed try with currect credentials")
def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"studentuname":sid})
def studentchangepwd(request):
    sid= request.session["sid"]
    return render(request,"studentchangepwd.html",{"studentuname":sid})
def studentupdatepwd(request):
    sid=request.session["sid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]


    print(sid,opwd,npwd)
    flag=Student.objects.filter(Q(username=sid)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Student.objects.filter(username=sid).update(password=npwd)
        print("password ubdated sussfully")
        msg="password updated successfully"
        return render(request, "studentchangepwd.html", {"studentuname": sid, "msg": msg,"color":"green"})
    else:
        print("Old pwd is Invalid")
        msg="Old password is Incurrect"
        return render(request,"studentchangepwd.html",{"studentuname":sid,"msg":msg,"color":"red"})
def dispalystudentcourses(request):
    sid = request.session["sid"]
    ay=request.POST["ay"]
    sem=request.POST["sem"]
    courses=Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))
    return render(request,"displaystudentcourses.html",{"courses":courses,"sid": sid })
