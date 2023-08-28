from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


# Create your views here.
class Home(TemplateView):
    template_name = 'homepage/index.html'
