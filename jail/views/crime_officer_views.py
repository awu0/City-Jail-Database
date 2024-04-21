from django.views import generic

from jail.models import CrimeOfficer


class CrimeOfficerHomeView(generic.ListView):
    template_name = 'crime_officer/index.html'
    context_object_name = 'crime_officer_list'

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'crime')  
        order = self.request.GET.get('order', 'asc')  
        
        if order == 'desc':
            sort = '-' + sort  
        return CrimeOfficer.objects.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'crime')
        context['current_order'] = self.request.GET.get('order', 'asc')
        return context


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
