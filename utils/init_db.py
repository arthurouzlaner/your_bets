from leagues.models import LeagueType, LeagueGame, Team
import json

def get_file_content(path): f=open(path,"r");content = f.read(); f.close(); return content


# with open ("get_events_group_a.txt") as groups_file:
#     groups = json.load(groups_file)
#     for i, group in enumerate(groups):
#         Team.objects.create(team_name=group['match_hometeam_name'])
#         Team.objects.create(team_name=group['match_awayteam_name'])

# LeagueType.objects.create(league_name="Champions League", league_type=1, game_id_list="[1,4,5,6]")

# LeagueGame.objects.create(game_date=datetime.now(), home_team_id=1, away_team_id=2, stage_name=0, round_number=1,game_result="")

def init_teams():
    Team.objects.create(team_name="Super Dupers")