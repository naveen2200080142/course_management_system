from django.contrib import admin

# Register your models here.
from .models import Admin,Faculty,Student,Course,FacultyCourseMapping
admin.site.register(Admin)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(FacultyCourseMapping)