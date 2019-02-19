from django.db import models

class Tournament(models.Model):
    name                    = models.CharField(max_length=120)
    description             = models.TextField(blank=True) # optional field
    subtournament_id_list   = models.TextField() #Json converted
    admin_id                = models.IntegerField()

class SubTournament(models.Model):
    league_id       = models.IntegerField()
    rules_id_list   = models.TextField() #Json converted