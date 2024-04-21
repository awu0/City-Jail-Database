from django.views import generic

from jail.models import Officer, CrimeOfficer


class OfficerHomeView(generic.ListView):
    template_name = 'officer/index.html'
    context_object_name = 'officer_list'

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'officer_id')  
        order = self.request.GET.get('order', 'asc')  
        
        if order == 'desc':
            sort = '-' + sort  
        return Officer.objects.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'officer_id')
        context['current_order'] = self.request.GET.get('order', 'asc')
        return context


class OfficerDetailView(generic.DetailView):
    model = Officer
    template_name = 'officer/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['crime_officer_list'] = CrimeOfficer.objects.filter(officer__officer_id=int(self.kwargs['pk']))

        return context


class OfficerUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = Officer
    template_name = 'officer/update.html'
    fields = '__all__'

    success_url = '/officer/'


class OfficerFormView(generic.CreateView):
    """
    For adding a new officer
    """
    template_name = 'officer/add.html'
    model = Officer
    fields = '__all__'
    success_url = '/officer/'


class OfficerDeleteView(generic.DeleteView):
    model = Officer

    template_name = 'officer/delete.html'
    success_url = '/officer/'
