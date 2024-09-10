from django.shortcuts import render
from django.http import HttpResponse
from .models import patient,staff,appointment

#dashboard
def index(request):
    #return HttpResponse("Oi")
    return render(request,"index.html",{})


#calendar
def calendar(request):
    return render(request,"calendar.html",{})

# Patients
def patients(request):
    context = {'patients':patient.objects.all()}
    return render(request,"patients.html",context)



# Staff Schedule
def staffSched(request):
    return render(request,"staffSched.html",{})

