from django.contrib import admin

from leagues.models import LeagueType, LeagueGame, Team

admin.site.register(LeagueType)
admin.site.register(LeagueGame)
admin.site.register(Team)
