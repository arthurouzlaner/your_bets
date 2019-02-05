from django.contrib import admin

from leagues.models import LeagueType,LeageStage,LeageRound,LeagueGame

admin.site.register(LeagueType)
admin.site.register(LeageStage)
admin.site.register(LeageRound)
admin.site.register(LeagueGame)
