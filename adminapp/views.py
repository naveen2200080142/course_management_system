from django.db.models import Q
from django.shortcuts import render,HttpResponse
from .models import Admin,Course,Student,Faculty,FacultyCourseMapping
from .forms import AddFacultyForm,AddStudentForm
# Create your views here.
def adminhome(request):
    return render(request, "adminhome.html")
def adminlogin(request):
    return render(request,"adminlogin.html")
def checkadminlogin(request):
    adminname=request.POST["uname"]
    adminpass = request.POST["pwd"]
    flag=Admin.objects.filter(Q(username=adminname)&Q(password=adminpass))
    if flag:
        print("login Succeses")
        request.session["auname"]=adminname
        return render(request,'adminhome.html',{"adminuname":adminname})
    else:
        return HttpResponse("login failed try with currect credentials")


def adminchangepass(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})


def adminstudent(request):
    auname=request.session["auname"]
    return render(request,"adminstudent.html",{"adminuname":auname})


def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname})


def admincourse(request):
    auname = request.session["auname"]
    return render(request,"admincourse.html",{"adminuname":auname})
def viewcourses(request):
    courses=Course.objects.all()
    ccount = Faculty.objects.count()
    ccount+=1
    return render(request,"viewcourses.html",{"coursesdata": courses,"count":ccount})
def viewfaculty(request):
    faculty=Faculty.objects.all()
    fcount=Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata": faculty,"count":fcount})
def viewstudents(request):
    Students=Student.objects.all()
    scount=Student.objects.count()
    return render(request,"viewstudents.html",{"studentdata": Students,"count":scount})

def addcourse(request):
    return render(request,"addcourse.html")

def insertcourse(request):
    # Get the data from the POST request
    dept = request.POST["dept"]
    program = request.POST["program"]
    ay = request.POST["ay"]
    sem = request.POST["sem"]
    year = request.POST["year"]
    ccode = request.POST["ccode"]
    ctitle = request.POST["ctitle"]
    LTPS=request.POST["ltps"]
    Credits=request.POST["credits"]

    # Create a new course object with the data
    course = Course(department=dept, program=program, academicyear=ay, semester=sem, year=year, coursecode=ccode, coursetitle=ctitle,ltps=LTPS,credits=Credits)

    # Save the course object to the database
    Course.save(course)
    msg="Course Added succesfully"
    # Return a success message or redirect to another view
    return render(request,"addcourse.html",{"msg":msg})
def deletecourse(request):
    courses=Course.objects.all()
    ccount = Course.objects.count()
    return render(request,"deletecourse.html",{"coursesdata": courses,"count":ccount})
def coursedeletion(request,cid):
    courses=Course.objects.all()
    ccount = Course.objects.count()
    Course.objects.filter(id=cid).delete()
    msg="Course delete Successfully"
    return render(request,"deletecourse.html",{"msg":msg,"coursesdata": courses,"count":ccount})
def addfaculty(request):
    form=AddFacultyForm()
    if request.method=="POST":
        form=AddFacultyForm(request.POST)
        if form.is_valid():
            form.save()
            message="Faculty Added Successfully"
            return render(request,"addfaculty.html",{"msg":message,"form":form,"color":"green"})
        else:
            message = "Faculty Added Failed"
            return render(request, "addfaculty.html", {"msg": message, "form": form,"color":"red"})

    return render(request,"addfaculty.html",{"form":form})
def deletefaculty(request):
    courses=Faculty.objects.all()
    ccount = Faculty.objects.count()
    return render(request,"deletefaculty.html",{"facultydata": courses,"count":ccount})
def facultydeletion(request,cid):
    courses=Faculty.objects.all()
    ccount =Faculty.objects.count()
    Faculty.objects.filter(id=cid).delete()
    msg="Faculty delete Successfully"
    return render(request,"deletefaculty.html",{"msg":msg,"facultydata": courses,"count":ccount})
def addstudent(request):
    form=AddStudentForm()
    if request.method=="POST":
        form=AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            message="Student Added Successfully"
            return render(request,"addstudent.html",{"msg":message,"form":form,"color":"green"})
        else:
            message = "Student Added Failed"
            return render(request, "addstudent.html", {"msg": message, "form": form,"color":"red"})


    return render(request,"addstudent.html",{"form":form})
def deletestudent(request):
    courses=Student.objects.all()
    ccount = Student.objects.count()
    return render(request,"deletestudent.html",{"studentdata": courses,"count":ccount})
def studentdeletion(request,cid):
    courses=Student.objects.all()
    ccount =Student.objects.count()
    Student.objects.filter(id=cid).delete()
    msg="Student delete Successfully"
    return render(request,"deletestudent.html",{"msg":msg,"studentdata": courses,"count":ccount})


def facultycoursemapping(request):
    fcourses=FacultyCourseMapping.objects.all()
    auname = request.session["auname"]
    return render(request,"facultycoursemapping.html",{"adminuname":auname,"fmcourses":fcourses})
def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})
def adminupdatepwd(request):
    auname=request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]


    print(auname,opwd,npwd)
    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("password ubdated sussfully")
        msg="password updated successfully"
        return render(request, "adminchangepwd.html", {"adminuname": auname, "msg": msg,"color":"green"})
    else:
        print("Old pwd is Invalid")
        msg="Old password is Incurrect"
        return render(request,"adminchangepwd.html",{"adminuname":auname,"msg":msg,"color":"red"})