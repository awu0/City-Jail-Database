from django.views import generic

from jail.models import CrimeCode, CrimeCharge


class CrimeCodeHomeView(generic.ListView):
    template_name = 'crime_code/index.html'
    context_object_name = 'crime_code_list'

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'crime_code')  
        order = self.request.GET.get('order', 'asc')  
        
        if order == 'desc':
            sort = '-' + sort  
        return CrimeCode.objects.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'crime_code')
        context['current_order'] = self.request.GET.get('order', 'asc')
        return context


class CrimeCodeDetailView(generic.DetailView):
    model = CrimeCode
    template_name = 'crime_code/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['crime_charge_list'] = CrimeCharge.objects.filter(crime_code__crime_code=int(self.kwargs['pk']))

        return context


class CrimeCodeUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = CrimeCode
    template_name = 'crime_code/update.html'
    fields = [
        'code_description'
    ]

    success_url = '/crime_code/'


class CrimeCodeFormView(generic.CreateView):
    """
    For adding a new crime code
    """
    template_name = 'crime_code/add.html'
    model = CrimeCode
    fields = '__all__'
    success_url = '/crime_code/'


class CrimeCodeDeleteView(generic.DeleteView):
    model = CrimeCode

    template_name = 'crime_code/delete.html'
    success_url = '/crime_code/'
