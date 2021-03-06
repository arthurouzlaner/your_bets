"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tournaments.views import hompage_view, tournaments_view, scoreboard_view
from leagues.views import league_view
from users.views import details_view, user_creation_view, user_edit_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', hompage_view, name='home'),
    path('tournaments/', tournaments_view, name='tournaments'),
    path('scoreboard/', scoreboard_view),
    path('league/', league_view),
    path('admin/', admin.site.urls),
    path('users/add/', user_creation_view),
    path('users/<int:id>/', user_edit_view),
    path('users/', details_view),
    path('users/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()

print("hello world")
