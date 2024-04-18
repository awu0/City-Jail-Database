from django.views import generic

from jail.models import Appeal


class AppealHomeView(generic.ListView):
    template_name = 'appeal/index.html'
    context_object_name = 'appeal_list'

    def get_queryset(self):
        return Appeal.objects.order_by('appeal_id')


class AppealUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = Appeal
    template_name = 'appeal/update.html'
    fields = [
        'filing_date',
        'hearing_date',
        'status'
    ]

    success_url = '/appeal/'


class AppealFormView(generic.CreateView):
    """
    For adding a new appeal
    """
    template_name = 'appeal/add.html'
    model = Appeal
    fields = '__all__'
    success_url = '/appeal/'


class AppealDeleteView(generic.DeleteView):
    model = Appeal

    template_name = 'appeal/delete.html'
    success_url = '/appeal/'
