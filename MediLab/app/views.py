from django.shortcuts import render
from django.http import HttpResponse

#dashboard
def index(request):
    #return HttpResponse("Oi")
    return render(request,"index.html",{})


#calendar
# def calendar(request):
#     return render()

# Patients
# def patients(request):
#     return render()

# Staff Schedule
# def staffSched(request):
#     return render()

