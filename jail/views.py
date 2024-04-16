from django.forms import ModelForm
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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


class CriminalDetailView(generic.DetailView):
    model = Criminal
    template_name = 'criminal/detail.html'


class CriminalFormView(generic.CreateView):
    template_name = 'criminal/add.html'
    form_class = CriminalForm
    success_url = '/criminal'
