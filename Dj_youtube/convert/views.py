from django.shortcuts import render
from django.http import HttpResponse
from .models import History
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'convert/index.html'
    context_object_name = 'all_history_list'

    def get_queryset(self):
        return History.objects.all()


class HistoryView(generic.ListView):
    model = History
    template_name = 'convert/history_list.html'




