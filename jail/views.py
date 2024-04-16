from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Criminal


def index(request):
    return HttpResponse("Home Page")


def criminal_home(request):
    criminal_list = Criminal.objects.order_by('criminal_id')
    context = {
        'criminal_list': criminal_list
    }
    return render(request, 'criminal/index.html', context)


def criminal_detail(request, criminal_id):
    criminal = get_object_or_404(Criminal, pk=criminal_id)
    return render(request, 'criminal/detail.html', {'criminal': criminal})
