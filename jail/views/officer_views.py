from django.views import generic

from jail.models import Officer


class OfficerHomeView(generic.ListView):
    template_name = 'officer/index.html'
    context_object_name = 'officer_list'

    def get_queryset(self):
        return Officer.objects.order_by('officer_id')


class OfficerDetailView(generic.DetailView):
    model = Officer
    template_name = 'officer/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class OfficerUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = Officer
    template_name = 'officer/update.html'
    fields = '__all__'

    success_url = '/officer/'


class OfficerFormView(generic.CreateView):
    """
    For adding a new criminal
    """
    template_name = 'officer/add.html'
    model = Officer
    fields = '__all__'
    success_url = '/officer/'


class OfficerDeleteView(generic.DeleteView):
    model = Officer

    template_name = 'officer/delete.html'
    success_url = '/officer/'
