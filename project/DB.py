from django.db.models import Count, Avg, F, Sum

from project.models import Matches, Deliveries


def match_per_season():
    season_data = Matches.objects.order_by("season").values("season").annotate(match_count=Count("season"))
    return season_data

def run_conceded_by_team():
    match_in_2016 = Matches.objects.filter(season=2016)
    teams = Deliveries.objects.filter(match_id_id__in=match_in_2016).only("bowling_team").values(
        "bowling_team").annotate(runs=Sum("extra_runs"))
    return teams

def economical_bowlers():
    match_in_2015 = Matches.objects.only("season", "id").filter(season=2015)
    bowlers = Deliveries.objects.filter(match_id_id__in=match_in_2015).values("bowler").annotate(
        avg=Avg("total_runs") * 6).order_by('avg')[:10]
    return bowlers

def match_won_per_team_per_season():
    result = {}
    seasons = []
    demoseasons=Matches.objects.order_by('season').values('season').distinct()
    for winner in demoseasons:
        seasons.append(winner['season'])
    teamsquery = Matches.objects.order_by('season').exclude(winner__isnull=True).exclude(winner__exact='').values('winner','season').annotate(win=Count('winner'))

    for entry in teamsquery:
        if entry['winner'] not in result.keys():
            result[entry['winner']] = [0]*len(seasons)
        result[entry['winner']][seasons.index(entry['season'])]=entry['win']
    return [result,seasons]

def toss_win_lead_to_match_win():
    win = Matches.objects.filter(toss_winner=F('winner')).count()
    total=Matches.objects.all().count()
    winning_data={'win':round(win/total * 100,2),'loss':round((total-win)/total * 100,2)}
    return winning_data

