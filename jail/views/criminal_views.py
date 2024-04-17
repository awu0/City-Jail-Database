from django.views import generic

from jail.models import Criminal, Alias


class CriminalHomeView(generic.ListView):
    template_name = 'criminal/index.html'
    context_object_name = 'criminal_list'

    def get_queryset(self):
        return Criminal.objects.order_by('criminal_id')


class CriminalDetailView(generic.DetailView):
    model = Criminal
    template_name = 'criminal/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object'] = Criminal.objects.get(pk=self.kwargs['pk'])
        context['alias_list'] = Alias.objects.filter(criminal_id=self.kwargs['pk'])

        return context


class CriminalUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = Criminal
    template_name = 'criminal/update.html'
    fields = [
        'first_name',
        'last_name',
        'street',
        'city',
        'state',
        'zip',
        'phone',
        'v_status',
        'p_status'
    ]

    success_url = '/criminal/'


class CriminalFormView(generic.CreateView):
    """
    For adding a new criminal
    """
    template_name = 'criminal/add.html'
    model = Criminal
    fields = '__all__'
    success_url = '/criminal/'


class CriminalDeleteView(generic.DeleteView):
    model = Criminal

    template_name = 'criminal/delete.html'
    success_url = '/criminal/'
