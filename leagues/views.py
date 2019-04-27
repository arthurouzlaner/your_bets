from django.http import HttpResponse
from django.shortcuts import render

def league_view(request, *args, **kwargs):
    return render(request, "league.html", {})
