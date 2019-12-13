
from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, PatientSearchView, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('medication/', include('prescription_gen.urls')),
    path('search/', SearchView.as_view(), name='search'),
    path('search/patient/', PatientSearchView.as_view(), name='search_results'),
]
