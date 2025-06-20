from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()
    special=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=10,null=True, blank=True)
    number=models.IntegerField(null=True)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date1=models.DateField()
    time1=models.TimeField()

    def __str__(self):
        return self.Doctor.name+"--"+self.Patient.name