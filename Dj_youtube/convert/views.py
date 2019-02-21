from django.shortcuts import render
from django.http import HttpResponse
from .models import History
from django.views import generic
# Create your views here.


def index(request):
    if request.method == 'GET':
        template_name = 'convert/index.html'
        return render(request, template_name)

    elif request.method == 'POST':
        #print(request.POST)
        urls = request.POST['url']
        #title = request(title__regex=r'Destination: (.*.mp3)')
        History.download_song(urls, urls)
        #History.save_to_db(urls, urls)
        return HttpResponse("Good")
    else:
        pass


def history(request):
    all_history_list = History.objects.all()
    context = {'all_history_list': all_history_list}
    return render(request, 'convert/history_list.html', context)



