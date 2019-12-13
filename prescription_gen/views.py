from django.shortcuts import render
from django.views.generic import CreateView

from .models import Medicine


class MedicineCreateView(CreateView):
    model = Medicine
    template_name = 'prescription_gen/medicine_new.html'
    fields = '__all__'
