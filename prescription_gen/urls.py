from django.urls import include, path

from .views import (MedicineCreateView, PrescriptionMedicineCreate,
                PrescriptionMedicineUpdateView, PrescriptionDetailView)

urlpatterns = [
    path('add/medicine/', MedicineCreateView.as_view(), name='add_medicine'),
    path('add/prescription/medicine', PrescriptionMedicineCreate.as_view(), name='add_pr_med'),
    path('update/prescription/<pk>/', PrescriptionMedicineUpdateView.as_view(), name='pr_update'),
    path('detail/prescription/<pk>/', PrescriptionDetailView.as_view(), name='pr_detail'),
    ]
