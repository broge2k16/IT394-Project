from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    # ex: /polls/5/results/
    
]
