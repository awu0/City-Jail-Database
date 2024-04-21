from django.views import generic

from jail.models import CrimeCharge


class CrimeChargeHomeView(generic.ListView):
    template_name = 'crime_charge/index.html'
    context_object_name = 'crime_charge_list'

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'charge_id')  
        order = self.request.GET.get('order', 'asc')  
        
        if order == 'desc':
            sort = '-' + sort  
        return CrimeCharge.objects.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'charge_id')
        context['current_order'] = self.request.GET.get('order', 'asc')
        return context


class CrimeChargeUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = CrimeCharge
    template_name = 'crime_charge/update.html'
    fields = [
        'crime_code',
        'charge_status',
        'fine_amount',
        'court_fee',
        'amount_paid',
        'pay_due_date',
    ]

    success_url = '/crime_charge/'


class CrimeChargeFormView(generic.CreateView):
    """
    For adding a new crime charge
    """
    template_name = 'crime_charge/add.html'
    model = CrimeCharge
    fields = '__all__'
    success_url = '/crime_charge/'


class CrimeChargeeDeleteView(generic.DeleteView):
    model = CrimeCharge

    template_name = 'crime_charge/delete.html'
    success_url = '/crime_charge/'
