def create_db():
    from leagues.models import LeagueType, LeagueGame
    from tournaments.models import SubTournament, Tournament
    from users.models import PersonalData
    from datetime import datetime

    ## Create two different leagues
    LeagueType.objects.create(league_name="premier_league", league_type=1, game_id_list="{[1,4,5,6]}")
    LeagueType.objects.create(league_name="champions_league", league_type=2, game_id_list="{[2,3,7,8,9,10]}")

    ## Create League Games
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=1, away_team_id=2, stage_name=0, round_number=1, game_result="")
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=3, away_team_id=4, stage_name=0, round_number=1, game_result="")
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=3, away_team_id=4, stage_name=0, round_number=1, game_result="")
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=2, away_team_id=1, stage_name=0, round_number=1, game_result="")
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=3, away_team_id=1, stage_name=0, round_number=1, game_result="")
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=4, away_team_id=2, stage_name=0, round_number=1, game_result="")
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=3, away_team_id=4, stage_name=0, round_number=2, game_result="")
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=1, away_team_id=2, stage_name=1, round_number=1, game_result="")
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=1, away_team_id=3, stage_name=1, round_number=2, game_result="")
    LeagueGame.objects.create(game_date=datetime.now(), home_team_id=4, away_team_id=3, stage_name=2, round_number=1, game_result="")

    ## Create tournament
    Tournament.objects.create(name="Testing Tournament", description="Tournament created for site testing", subtournament_id_list="{[1,2]}", admin_id=0)

    ## Create sub tournament
    SubTournament.objects.create(league_id=1, rules_id_list="{[1]}")
    SubTournament.objects.create(league_id=2, rules_id_list="{[1]}")

    ## Create user
    PersonalData.objects.create(name="Jane", nickname="JohnDoe", email="sirozen9@gmail.com")


