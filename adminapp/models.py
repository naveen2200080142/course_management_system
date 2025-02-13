from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = "admin_table"
    def __str__(self):
        return self.username
class Course(models.Model) :
      id = models.AutoField(primary_key=True)
      department_choices=(("CSE(Reguler)","CSE(R)"),("AIDS(Reguler)","AIDS(R)"),("CSE(HONORS)","CSE(H)"),("MECH","Mech"))
      department = models.CharField(max_length=100, blank=False,choices=department_choices)
      program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
      program = models.CharField(max_length=50, blank=False, choices=program_choices, default="B.Tech")
      ac_choices=(("2024-25","2024-25"),("2023-24","2023-24"))
      academicyear = models.CharField(max_length=20, blank=False,choices=ac_choices)
      sem_choices = (("even", "even"), ("odd", "odd"))
      semester = models.CharField(max_length=10, blank=False,choices=sem_choices)
      year = models.IntegerField(blank=False)
      coursecode=models.CharField(max_length=20,blank=False)
      coursetitle=models.CharField(max_length=100,blank=False)
      ltps=models.CharField(max_length=10,blank=False,default="1-1-1-1")
      credits=models.FloatField(max_length=10,blank=False,default="4")
      class Meta:
         db_table="course_table"

      def __str__(self):
             return self.coursecode
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.BigIntegerField(blank=False,unique=True)
    fullname = models.CharField(max_length=100,blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("Others", "Others"))
    gender = models.CharField(max_length=20,blank=False,choices=gender_choices)
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(HONORS)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=50,blank=False,choices=department_choices,default="cse")
    program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=50, blank=False,choices=program_choices,default="B.Tech")
    sem_choices = (("Odd", "Odd"), ("Even", "Even"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices,default="Odd")
    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100,blank=False,default="klu123")
    email = models.CharField(max_length=100, blank=False,unique=True)
    contact = models.CharField(max_length=30,blank=False,unique=True)

    class Meta:
        db_table = "student_table"
    def __str__(self):
        return str(self.id)
class Faculty(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    facultyid = models.IntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = (("male", "male"), ("female", "female"), ("others", "others"))
    gender = models.CharField(max_length=20, blank=False, choices=gender_choices)
    department_choices = (("CSE(Reguler)", "CSE(R)"), ("AIDS(Reguler)", "AIDS(R)"), ("CSE(HONORS)", "CSE(H)"), ("MECH", "Mech"))
    department = models.CharField(max_length=100, blank=False, choices=department_choices)
    desi_choices=(("peof.", "professor"), ("Assoc. prof.", "Associate. professor"), ("assit. professor.", "assitent professor"))
    quali_choices=(("ph.d","ph.d"),("M.Tech","M.Tech"))
    qualification = models.CharField(max_length=50, blank=False,choices=quali_choices)

    designation = models.CharField(max_length=50, blank=False,choices=desi_choices)
    semester = models.CharField(max_length=10, blank=False)
    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100, default="klu123")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "faculty_table"
    def __str__(self):
        return str(self.id)
class FacultyCourseMapping(models.Model):
    mapping_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Replace "Course" with the actual Course model
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)  # Replace "Faculty" with the actual Faculty model
    type= models.BooleanField(default=True)  # True means Main Faculty
    COMPONENT_CHOICES = (
        ("L", "Lecture"),
        ("T", "Tutorial"),
        ("P", "Practical"),
    )
    session=models.IntegerField(blank=False,default=1)
    component= models.CharField(max_length=1, choices=COMPONENT_CHOICES,default="L")
    class Meta:
        db_table = "facultycoursemapping_table"

    def __str__(self):
        return f"{self.course.coursetitle} - {self.faculty.fullname}"


