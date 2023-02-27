from django import forms


class RegistrationForm(forms.Form):
    firstname = forms.CharField(label="Enter First Name", max_length=50)
    secondname = forms.CharField(label="Enter your Last Name", max_length=50)
    email = forms.CharField(label="Enter Email", max_length=30)
    age = forms.CharField(label="Age")
    DoB = forms.CharField(label="Enter Date of Birth", max_length=20)