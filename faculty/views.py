from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from adminapp.models import Admin,Course,Student,Faculty,FacultyCourseMapping
# Create your views here.
def facultyhome(request):

    return render(request, "facultyhome.html")
def facultylogin(request):
    return render(request,"facultylogin.html")
def checkfacultylogin(request):
    adminname=request.POST["fid"]
    adminpass = request.POST["pwd"]
    flag=Faculty.objects.filter(Q(facultyid=adminname)&Q(password=adminpass))
    if flag:
        request.session["fid"]=adminname
        return render(request,'facultyhome.html')
    else:
        return HttpResponse("login failed try with currect credentials")

def facultychangepwd(request):
    return render(request,"facultychangepwd.html")
def Ffacultycourses(request):
    fid = request.session.get("fid")
    if fid is not None:
        fmcourse = FacultyCourseMapping.objects.filter(faculty__facultyid=int(fid))
        count = fmcourse.count()
        return render(request, "Ffacultycourses.html", {"fid": fid, "fmcourses": fmcourse, "count": count})
    else:
        return HttpResponse("Faculty ID not found in the session. Please log in first.")

def facultychangepwd(request):
    fid= request.session["fid"]
    return render(request,"facultychangepwd.html",{"adminuname":fid})
def facultyupdatepwd(request):
    fid=request.session["fid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]


    print(fid,opwd,npwd)
    flag=Admin.objects.filter(Q(username=fid)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Faculty.objects.filter(username=fid).update(password=npwd)
        print("password ubdated sussfully")
        msg="password updated successfully"
        return render(request, "facultychangepwd.html", {"adminuname": fid, "msg": msg,"color":"green"})
    else:
        print("Old pwd is Invalid")
        msg="Old password is Incurrect"
        return render(request,"facultychangepwd.html",{"adminuname":fid,"msg":msg,"color":"red"})
