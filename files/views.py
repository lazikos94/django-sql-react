from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Posts_Model

class DbPageView(ListView):
    model = Posts_Model
    template_name = 'sample.html'
    context_object_name = 'all_posts_list'

class ReactPageView(TemplateView):
    model = Posts_Model
    template_name = 'view.html'
    context_object_name = 'view_stuff'

class PostCreateView(CreateView):
    model = Posts_Model
    template_name = 'post.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Posts_Model
    template_name = 'update.html'
    fields = ['title','body']

class PostDeleteView(DeleteView):
    model= Posts_Model
    template_name = 'delete.html'
    success_url = reverse_lazy('dbview')