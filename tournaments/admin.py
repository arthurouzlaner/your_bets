from django.contrib import admin

from .models import Tournament
from .models import SubTournament

admin.site.register(Tournament)
admin.site.register(SubTournament)