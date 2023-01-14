from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ratio', views.win_loss_ratio, name='ratio'), 
    path('upcoming', views.next_game_day, name='upcoming'),
    path('search_team', views.search_team, name='search_team'), 
    
]
