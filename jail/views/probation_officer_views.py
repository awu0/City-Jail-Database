from django.views import generic
from django.db.models import F
from jail.models import ProbationOfficer, Sentence


class ProbationOfficerHomeView(generic.ListView):
    template_name = 'probation_officer/index.html'
    context_object_name = 'probation_officer_list'

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'prob_id')  
        order = self.request.GET.get('order', 'asc')  
        
        if order == 'desc':
            sort = '-' + sort  
        return ProbationOfficer.objects.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'prob_id')
        context['current_order'] = self.request.GET.get('order', 'asc')
        return context


class ProbationOfficerDetailView(generic.DetailView):
    model = ProbationOfficer
    template_name = 'probation_officer/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sentence_list'] = Sentence.objects.filter(prob_officer__prob_id=self.kwargs['pk'])

        return context


class ProbationOfficerUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = ProbationOfficer
    template_name = 'probation_officer/update.html'
    fields = '__all__'

    success_url = '/probation_officer/'


class ProbationOfficerFormView(generic.CreateView):
    """
    For adding a new probation officer
    """
    template_name = 'probation_officer/add.html'
    model = ProbationOfficer
    fields = '__all__'
    success_url = '/probation_officer/'


class ProbationOfficerDeleteView(generic.DeleteView):
    model = ProbationOfficer

    template_name = 'probation_officer/delete.html'
    success_url = '/probation_officer/'
