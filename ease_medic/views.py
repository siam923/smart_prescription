from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from users.models import Patient


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchView(TemplateView):
    template_name = 'search_form.html'

class PatientSearchView(ListView):
    model = Patient
    template_name = 'patient_search_results.html'

    def get_queryset(self):
        """It’s also possible to customize the queryset
            by overriding the get_queryset()
            some builtin query-> filter(), all(), get(), exclude()"""
        query = self.request.GET.get('q')
        object_list = Patient.objects.filter(user__NID=query) 
        return object_list
