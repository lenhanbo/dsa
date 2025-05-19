from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.http import HttpResponse
from .models import item as item_list
from .models import user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.



class item_listview(LoginRequiredMixin, generic.ListView):
    
    model = item_list
    paginate_by = 12
    context_object_name = 'items' # ten de truy cap cua model
    # query_set = item_list.objects.order_by('price')
    template_name = 'blog/homepage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'shopping is good'
        
        visit_count = self.request.session.get('visit_count', 0)
        visit_count += 1
        self.request.session['visit_count'] = visit_count
        context['visit_count'] = visit_count
        return context

class item_detailview(LoginRequiredMixin, generic.DetailView):
    model = item_list
    context_object_name = 'item'
    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class user_detailview(LoginRequiredMixin, generic.DeleteView):
    model = user
    context_object_name = 'author'
    template_name = 'author_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class user_item(LoginRequiredMixin, generic.ListView):
    model =item_list
    context_object_name = 'item'

    template_name = 'user_item.html'
    def get_queryset(self):
        return (
            item_list.objects.filter(author = self.request.user)
            .order_by('price')
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context