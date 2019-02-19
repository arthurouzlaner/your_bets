def create_db():
    from leagues.models import LeagueType,LeagueGame
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



