from project.DB import match_per_season,run_conceded_by_team,economical_bowlers,toss_win_lead_to_match_win,match_won_per_team_per_season
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def index(request):
    return render(request,'project/index.html',{'seasons':match_per_season()})

@cache_page(CACHE_TTL)
def question1(request):
    return render(request, 'project/ques1.html', {'seasons': match_per_season()})

@cache_page(CACHE_TTL)
def question2(request):
    return render(request, 'project/ques2.html', {'match_won_per_teams_per_season': match_won_per_team_per_season()[0],'seasons':match_won_per_team_per_season()[1]})
@cache_page(CACHE_TTL)
def question3(request):
    return render(request,'project/ques3.html',{'run_per_team':run_conceded_by_team()})

@cache_page(CACHE_TTL)
def question4(request):
    return render(request,'project/ques4.html',{'economical_bowlers':economical_bowlers()})

@cache_page(CACHE_TTL)
def question5(request):
    return render(request,'project/ques5.html',{'wining':toss_win_lead_to_match_win()})
