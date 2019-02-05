from django.db import models

class LeagueType(models.Model):
    league_name     = models.CharField(default="", max_length=128)
    league_type     = models.IntegerField()
    stage_id_list   = models.TextField(default="") # json converted - id list to string

class LeageStage(models.Model):
    stage_name          = models.CharField(max_length=128)
    stage_start_date    = models.DateTimeField()
    stage_end_date      = models.DateTimeField()
    round_id_list       = models.TextField() #json converted - id list to string

class LeageRound(models.Model):
    round_number        = models.IntegerField()
    round_start_date    = models.DateTimeField()
    round_end_date      = models.DateTimeField()
    game_id_list        = models.TextField() #json convered - id list to string

class LeagueGame(models.Model):
    game_date       = models.DateTimeField()
    home_team_id    = models.IntegerField()
    away_team_id    = models.IntegerField()
    game_result     = models.TextField() #json converted - score to string
