from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Shablon_1(TemplateView):
    template_name = 'shablon_1.html'


def shablon_2(request):
    return render(request, 'shablon_2.html')