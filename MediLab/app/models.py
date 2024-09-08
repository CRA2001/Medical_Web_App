from django.db import models

# Create your models here.


#patient model
class patient(models.Model):
    patient_ID = models.BigAutoField(primary_key=True) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #you can implement the 'django-phonenumber-field' package 
    #here's the link: https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)

#staff model
class staff(models.Model):
    staff_ID = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    position = models.CharField(max_length=20)

class appointment(models.Model):
    appt_ID = models.BigAutoField(primary_key=True)
    staff_ID = models.ForeignKey(staff,on_delete=models.CASCADE)
    patient_ID = models.ForeignKey(patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()