from django.db import models
from django.urls import reverse

from users.models import User, Patient, Doctor

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    miligram = models.PositiveIntegerField(default=5)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name


class PrescriptionMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    timing = models.CharField(max_length=20, default = '1 + 0 + 1')
    duration = models.CharField(max_length=20, default = '1 week')


class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(PrescriptionMedicine, blank=True)

    def __str__(self):
        return "prescription for {} by {}".format(self.patient.user.first_name, self.doctor.user.first_name)
