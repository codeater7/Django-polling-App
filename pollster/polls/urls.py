from django.urls import path

# from all import views
from . import views

# steps 
#  tala ko garnee; 
#  yetti lee khasai kei gardaina, yeslai main ko urls ma  laijanee(vanako pollster app ma laijanee, )

app_name = 'polls'

#  '' empty lee chai / polls hunxa vanako ho,  connect to which views?  name deeako 
#  path lee k k khanxa?? link, kun view ra name

urlpatterns = [
    path('', views.index, name='index'),
    # angle brackets, because we are passing in the parameter, polls/id
    # question id will be abstracted from here, lets say

    # views.result vanako function ho
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
# path('result') vako vayee it would have been polls/result
# want to be /polls , connect to views.index and give the name index





path(link, view, name)


path('')