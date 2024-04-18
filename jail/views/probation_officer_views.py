from django.views import generic

from jail.models import ProbationOfficer


class ProbationOfficerHomeView(generic.ListView):
    template_name = 'probation_officer/index.html'
    context_object_name = 'probation_officer_list'

    def get_queryset(self):
        return ProbationOfficer.objects.order_by('prob_id')


class ProbationOfficerDetailView(generic.DetailView):
    model = ProbationOfficer
    template_name = 'probation_officer/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ProbationOfficerUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = ProbationOfficer
    template_name = 'probation_officer/update.html'
    fields = '__all__'

    success_url = '/probation_officer/'


class ProbationOfficerFormView(generic.CreateView):
    """
    For adding a new criminal
    """
    template_name = 'probation_officer/add.html'
    model = ProbationOfficer
    fields = '__all__'
    success_url = '/probation_officer/'


class ProbationOfficerDeleteView(generic.DeleteView):
    model = ProbationOfficer

    template_name = 'probation_officer/delete.html'
    success_url = '/probation_officer/'
