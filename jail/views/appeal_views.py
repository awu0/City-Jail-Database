from django.views import generic

from jail.models import Appeal


class AppealHomeView(generic.ListView):
    template_name = 'appeal/index.html'
    context_object_name = 'appeal_list'

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'appeal_id')  
        order = self.request.GET.get('order', 'asc')  
        
        if order == 'desc':
            sort = '-' + sort  
        return Appeal.objects.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'appeal_id')
        context['current_order'] = self.request.GET.get('order', 'asc')
        return context


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
