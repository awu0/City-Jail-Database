from django.views import generic

from jail.models import Crime, CrimeCharge


class CrimeHomeView(generic.ListView):
    template_name = 'crime/index.html'
    context_object_name = 'crime_list'

    def get_queryset(self):
        return Crime.objects.order_by('criminal')


class CrimeDetailView(generic.DetailView):
    model = Crime
    template_name = 'crime/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['crime_charge_list'] = CrimeCharge.objects.filter(crime__crime_id=int(self.kwargs['pk']))

        return context


class CrimeUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = Crime
    template_name = 'crime/update.html'
    fields = [
        'classification',
        'date_charged',
        'status',
        'hearing_date',
        'appeal_cut_date',
    ]

    success_url = '/crime/'


class CrimeFormView(generic.CreateView):
    """
    For adding a new crime
    """
    template_name = 'crime/add.html'
    model = Crime
    fields = '__all__'
    success_url = '/crime/'


class CrimeDeleteView(generic.DeleteView):
    model = Crime

    template_name = 'crime/delete.html'
    success_url = '/crime/'
