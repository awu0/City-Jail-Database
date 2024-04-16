from django.http import HttpResponse
from django.views import generic

from .forms import CriminalForm
from .models import Criminal


def index(request):
    return HttpResponse("Home Page")


class CriminalHomeView(generic.ListView):
    template_name = 'criminal/index.html'
    context_object_name = 'criminal_list'

    def get_queryset(self):
        return Criminal.objects.order_by('criminal_id')


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

    success_url = '/criminal'


class CriminalFormView(generic.CreateView):
    template_name = 'criminal/add.html'
    form_class = CriminalForm
    success_url = '/criminal'
