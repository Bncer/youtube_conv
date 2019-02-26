from django.shortcuts import render
from django.http import HttpResponse
from .models import History
from . import service


def home(request):
    template_name = 'convert/home.html'
    if request.method == 'POST':
        urls = request.POST['url']
        service.download_song(urls)
        return HttpResponse("You have downloaded")
    return render(request, template_name)


def show_history(request):
    return render(request, 'convert/history_list.html', {'all_history_list': History.objects.all()})




