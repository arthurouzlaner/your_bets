from django.contrib import admin

from leagues.models import LeagueType,LeagueGame

admin.site.register(LeagueType)
admin.site.register(LeagueGame)
