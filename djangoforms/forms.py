from django import forms

class StudentForm(forms.Form):
    firstname= forms.CharField(label="Enter First Name",max_length=50)
    secondname= forms.CharField(label="Enter your Last Name",max_length=50)
    email= forms.CharField(label="Enter Email",max_length=30)

