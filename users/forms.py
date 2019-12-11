from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import (Doctor, Patient, User)


#for public view
class PatientSignUpForm(UserCreationForm):
    address = forms.CharField(label='Address')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('NID', 'email', 'age', 'gender',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.address.add(*self.cleaned_data.get('address'))
        return user


class DoctorSignUpFrom(UserCreationForm):
    SSC_GPA = forms.DecimalField(label="SSC GPA")
    HSC_GPA = forms.DecimalField(label="HSC GPA")
    BMDC_RegNo = forms.CharField(label='BMDC Reg No')
    MBBS_Session = forms.CharField(label='MBBS Session')
    MBBS_Inst = forms.CharField(label='Institution')
    PostGrad_details = forms.CharField(label='PostGrad Info')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('NID', 'email', 'age', 'gender',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.SSC_GPA.add(*self.cleaned_data.get('SSC_GPA'))
        doctor.HSC_GPA.add(*self.cleaned_data.get('HSC_GPA'))
        doctor.BMDC_RegNo.add(*self.cleaned_data.get('BMDC_RegNo'))
        doctor.MBBS_Session.add(*self.cleaned_data.get('MBBS_Session'))
        doctor.MBBS_Inst.add(*self.cleaned_data.get('MBBS_Inst'))
        doctor.PostGrad_details.add(*self.cleaned_data.get('PostGrad_details'))
