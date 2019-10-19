from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Posts_Model

class DbPageView(ListView):
    model = Posts_Model
    template_name = 'sample.html'
    context_object_name = 'all_posts_list' # new

class ReactPageView(TemplateView):
    model = Posts_Model
    template_name = 'view.html'
    context_object_name = 'view_stuff'