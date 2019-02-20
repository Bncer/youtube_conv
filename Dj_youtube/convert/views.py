from django.shortcuts import render
from django.http import HttpResponse
from .models import History
from django.views import generic
# Create your views here.


class IndexView(generic.TemplateView):


    def get(self, request):
        template_name = 'convert/index.html'
        return render(request, template_name)

    def post(self, request):
        print(request.POST)
        urls = request.POST['url']
        History.download_song(urls, urls)
        History.save_to_db(urls, urls)
        return HttpResponse("Good")


class HistoryView(generic.ListView):
    model = History
    template_name = 'convert/history_list.html'
    context_object_name = 'all_history_list'

    def get_queryset(self):
        return History.objects.all()



