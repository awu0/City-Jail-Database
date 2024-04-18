from django.views import generic

from jail.models import CrimeOfficer


class CrimeOfficerHomeView(generic.ListView):
    template_name = 'crime_officer/index.html'
    context_object_name = 'crime_officer_list'

    def get_queryset(self):
        return CrimeOfficer.objects.order_by('crime')



class CrimeOfficerFormView(generic.CreateView):
    """
    For adding a new Crime & Officer Association
    """
    template_name = 'crime_officer/add.html'
    model = CrimeOfficer
    fields = '__all__'
    success_url = '/crime_officer/'


class CrimeOfficerDeleteView(generic.DeleteView):
    model = CrimeOfficer

    template_name = 'crime_officer/delete.html'
    success_url = '/crime_officer/'
