from django.contrib import admin
from app.models import patient, staff, appointment

# Register your models here.
admin.site.register(patient)
admin.site.register(staff)
admin.site.register(appointment)