from django.urls import include, path

from .views import MedicineCreateView

urlpatterns = [
    path('add/medicine/', MedicineCreateView.as_view(), name='add_medicine'),
    ]
