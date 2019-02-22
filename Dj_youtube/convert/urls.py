from django.urls import path

from . import views


app_name = 'convert'
urlpatterns = [
        path('', views.home, name='home'),
        path('history/', views.show_history, name='history')
]



