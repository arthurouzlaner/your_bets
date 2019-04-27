from django.http import HttpResponse
from django.shortcuts import render

def hompage_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def tournaments_view(*args, **kwargs):
    return HttpResponse("<h1>Tournaments</h1>")

def scoreboard_view(request, *args, **kwargs):
    return render(request, "scoreboard.html", {})