from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView
from django.views.generic.base import TemplateResponseMixin, View

from .models import Medicine, PrescriptionMedicine, Prescription
from .forms import MedicineFormSet

class MedicineCreateView(CreateView):
    model = Medicine
    template_name = 'prescription_gen/medicine_new.html'
    fields = '__all__'


class PrescriptionMedicineCreate(CreateView):
    model = PrescriptionMedicine
    template_name = 'prescription_gen/pr_medicine.html'
    fields = '__all__'


class PrescriptionMedicineUpdateView(TemplateResponseMixin, View):
    template_name = 'prescription_gen/formset.html'
    prescription = None

    def get_formset(self, data=None):
        return MedicineFormSet(instance=self.prescription, data=data)

    def dispatch(self, request, pk):
        self.prescription = get_object_or_404(Prescription, id=pk)
        return super(PrescriptionMedicineUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'prescription': self.prescription,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('home') ## Update with prescription detail
        return self.render_to_response({'prescription': self.prescription,
                                        'formset': formset})

class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'prescription_gen/prescription_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PrescriptionDetailView, self).get_context_data(*args, **kwargs)
        id = self.kwargs['pk']
        context['medicines'] = PrescriptionMedicine.objects.filter(prescription__id=id)
        return context
