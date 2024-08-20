from django.shortcuts import render
from django.http import HttpResponse

#dashboard
def index(request):
    #return HttpResponse("Oi")
    return render(request,"index.html",{})


#calendar
def calendar(request):
    return render(request,"calendar.html",{})

# Patients
def patients(request):
    return render(request,"patients.html",{})

# Staff Schedule
def staffSched(request):
    return render(request,"staffSched.html",{})

