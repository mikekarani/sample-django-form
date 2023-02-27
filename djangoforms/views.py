from django.shortcuts import render
from djangoforms.forms import StudentForm


def index(request):
    student=StudentForm()
    return render(request, 'index.html', {'form': student})
def sample(request):
    registration = RegistrationForm()
    return render(request, 'sampleform.html', {'form1': registration})
