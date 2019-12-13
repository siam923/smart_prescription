from django.urls import include, path

from .views import SignUpView, DoctorSignUpView, PatientSignUpView, DoctorsListView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/doctor', DoctorSignUpView.as_view(), name='signup_doctor'),
    path('signup/patient', PatientSignUpView.as_view(), name='signup_patient'),
    path('doctors/', DoctorsListView.as_view(), name='doctor_list'),
]
