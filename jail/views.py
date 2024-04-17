from django.shortcuts import redirect
from django.views import generic

from .forms import CriminalForm
from .models import Criminal, Alias


def index(request):
    return redirect('/criminal/')


class CriminalHomeView(generic.ListView):
    template_name = 'criminal/index.html'
    context_object_name = 'criminal_list'

    def get_queryset(self):
        return Criminal.objects.order_by('criminal_id')


class CriminalDetailView(generic.DetailView):
    model = Criminal
    template_name = 'criminal/detail.html'

    def get_context_data(self, **kwargs):
        return {
            'object': Criminal.objects.get(pk=self.kwargs['pk']),
            'alias_list': Alias.objects.filter(criminal_id=self.kwargs['pk'])
        }


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
    form_class = CriminalForm
    success_url = '/criminal/'


class CriminalDeleteView(generic.DeleteView):
    model = Criminal

    template_name = 'criminal/delete.html'
    success_url = '/criminal/'
