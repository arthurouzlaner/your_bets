from django.db import models

class LeagueType(models.Model):
    league_name     = models.CharField(default="", max_length=128)
    league_type     = models.IntegerField()
    game_id_list    = models.TextField(default="") # json converted - id list to string

class LeagueGame(models.Model):
    game_date       = models.DateTimeField()
    home_team_id    = models.IntegerField()
    away_team_id    = models.IntegerField()
    stage_name      = models.IntegerField() # ENUM
    round_number    = models.IntegerField()
    game_result     = models.TextField() #json converted - score to string
