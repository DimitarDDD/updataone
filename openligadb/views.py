from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from django.utils import timezone
import datetime
from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings
# Create your views here.

#get all teams from the api
def api_all_teams():
    response = requests.get(settings.API_URL + '/' + 'getavailableteams' + '/' + settings.LEAGUE + '/' + settings.SEASON)
    return response.json()

#get all games from the api
def api_all_games():
    response = requests.get(settings.API_URL + '/' + 'getmatchdata' + '/' + settings.LEAGUE + '/' + settings.SEASON)
    return response.json()

#get all statics from the api
def api_all_statistics():
    response = requests.get(settings.API_URL + '/' + 'getbltable' + '/' + settings.LEAGUE + '/' + settings.SEASON)
    return response.json()

# home page url - home page ur 
def home(request):
    all_games = api_all_games()
    context = {
       'all_games':all_games,
    }
    return render(request, 'home.html', context)

# search for a team return the search page
def search_team(request):
    team_name = request.GET.get('q')
    if team_name:
        if is_team_in_league(team_name):
            next_game = team_next_game(team_name)
            team_statistics = team_statistic(team_name)
            team_statistics['win_loss'] = ratio(team_statistics['Won'], team_statistics['Lost'])

            context = {
                'next_game': next_game,
                'team_stats': team_statistics,
                'season': settings.SEASON,
                }
        else:
            messages.error(request, "Have done a typing mistake or your team is not in the database")
            return HttpResponseRedirect(reverse_lazy('home'))
        return render(request, 'search_team.html', context)
    return render(request, 'search_team.html')

# return the ration between won and lost games
def win_loss_ratio(request):
    all_statistics = api_all_statistics()
    for s in all_statistics:
        s['win_loss'] = ratio(s['Won'], s['Lost'])
    context = {'statistic': all_statistics}
    return render(request, 'win_loss_ratio.html', context)

# return the future.upcoming games
def next_game_day(request):
    now = timezone.now().date()
    upcoming = []
    all_games = api_all_games()
    for i in all_games:
        for k, v in i.items():
            if k == 'MatchDateTimeUTC':
                z = date_of_game(v)
                if z > now:
                    upcoming.append(i)
    context = {
        'upcoming': upcoming,
    }
    return render(request, 'upcomingmatch.html', context)

# check if match has finished or not
def team_next_game(team_name):
    all_games = api_all_games()
    for game in all_games:
        team1_name = game['Team1']['TeamName']
        team2_name = game['Team2']['TeamName']
        if team1_name == team_name or team2_name == team_name:
            if game['MatchIsFinished']:
                continue
            return game
    return None

# get all the games for a particular team
def team_season_games(team_name):
    all_games = api_all_games()
    all_games_of_team = []
    for game in all_games:
        team1_name = game['Team1']['TeamName']
        team2_name = game['Team2']['TeamName']
        if team1_name == team_name or team2_name == team_name:
            all_games_of_team.append(game)
    return all_games_of_team

# check if the team from the search is in the databse-api
def is_team_in_league(team):
    all_teams = api_all_teams()
    all_team_names = []
    for t in all_teams:
        all_team_names.append((t['TeamName']).lower())
    if team.lower() in all_team_names:
        return True
    return False

# get the statistics for a particular team
def team_statistic(team_name):
    all_statistics = api_all_statistics()
    for stats in all_statistics:
        if stats['TeamName'] == team_name:
            return stats
    return None

# calculate the win lose ratio
def ratio(win, loss):
    if loss == 0:
        return int(win)
    else:
        return round(float(win / loss), 2)

# format the date of game
def date_of_game(date):
    date1 =datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    date_strip = date1.date()
    return date_strip