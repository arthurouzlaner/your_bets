from django.shortcuts import render
from .models import PersonalData
from .forms import UserForm


def user_creation_view(request, *args, **kwargs):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    context = {'form': form}
    return render(request, "user_create.html", context)

def details_view(request, *args, **kwargs):
    users = PersonalData.objects.all()
    return render(request, "user_details.html", {'users': users})
