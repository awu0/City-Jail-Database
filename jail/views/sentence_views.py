from django.views import generic

from jail.models import Sentence


class SentenceHomeView(generic.ListView):
    template_name = 'sentence/index.html'
    context_object_name = 'sentence_list'

    def get_queryset(self):
        sort = self.request.GET.get('sort', 'criminal')  
        order = self.request.GET.get('order', 'asc')  
        
        if order == 'desc':
            sort = '-' + sort  
        return Sentence.objects.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'criminal')
        context['current_order'] = self.request.GET.get('order', 'asc')
        return context


class SentenceUpdateView(generic.UpdateView):
    # TODO: restrict to certain users
    model = Sentence
    template_name = 'sentence/update.html'
    fields = [
        'type',
        'start_date',
        'end_date',
        'violations'
    ]

    success_url = '/sentence/'


class SentenceFormView(generic.CreateView):
    """
    For adding a new sentence
    """
    template_name = 'sentence/add.html'
    model = Sentence
    fields = '__all__'
    success_url = '/Sentence/'


class SentenceDeleteView(generic.DeleteView):
    model = Sentence

    template_name = 'sentence/delete.html'
    success_url = '/sentence/'
