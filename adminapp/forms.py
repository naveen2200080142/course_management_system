from django import forms
from .models import Faculty,Student

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty # model name
        fields = '__all__' # all fields in the model
        exclude={"password"}
        labels = {'facultyid': 'Enter Faculty ID', 'gender': 'Select Gender', 'fullname': 'Enter Full Name'}
class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student # model name
        fields = '__all__' # all fields in the model
        exclude={"password"}
        labels = {'studentid': 'Enter student ID', 'gender': 'Select Gender', 'fullname': 'Enter Full Name'}
