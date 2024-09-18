from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Shablon1(TemplateView):
    template_name = 'shablon1.html'


class Shablin2(TemplateView):
    template_name = 'shablon2.html'