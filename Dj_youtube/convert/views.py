from django.shortcuts import render
from django.http import HttpResponse
from .models import History
from . import service
import requests



def home(request):
    template_name = 'convert/home.html'
    if request.method == 'POST':
        urls = request.POST['url']
        try:
            if urls[0:23] == 'https://www.youtube.com':
                meta = service.youdl_manage(urls)
                service.save_in_history(urls, meta)
                return HttpResponse("You have downloaded")
            else:
                pass
        except requests.exceptions.HTTPError as err:
            print(err)
    return render(request, template_name)


def show_history(request):
    return render(request, 'convert/history_list.html', {'all_history_list': History.objects.all()})




