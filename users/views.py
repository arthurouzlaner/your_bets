from django.shortcuts import render
from .models import PersonalData


def details_view(request, *args, **kwargs):
    users = PersonalData.objects.all()
    return render(request, "user_details.html", {'users': users})
