from django.views import generic
from jail.models import Alias

class AliasHomeView(generic.ListView):
    template_name = 'alias/index.html'
    context_object_name = 'alias_list'

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'criminal')  
        order = self.request.GET.get('order', 'asc')  
        
        if order == 'desc':
            sort = '-' + sort  
        return Alias.objects.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'criminal')
        context['current_order'] = self.request.GET.get('order', 'asc')
        return context


class AliasUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = Alias
    template_name = 'alias/update.html'
    fields = [
        'alias'
    ]

    success_url = '/alias/'


class AliasFormView(generic.CreateView):
    """
    For adding a new alias
    """
    template_name = 'alias/add.html'
    model = Alias
    fields = '__all__'
    success_url = '/alias/'


class AliasDeleteView(generic.DeleteView):
    model = Alias

    template_name = 'alias/delete.html'
    success_url = '/alias/'
