from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Sample

class HomePageView(ListView):
    model = Sample
    template_name = 'sample.html'
    context_object_name = 'all_posts_list' # new
