from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="index"),
    path("calendar/",views.calendar,name="calendar"),
    path("patients/",views.patients,name="patients"),
    path("staffSched/",views.staffSched,name="staffSched")
]