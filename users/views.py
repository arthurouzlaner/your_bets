from django.http import HttpResponseRedirect
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

def user_edit_view(request, id, *args, **kwargs):
    instance = PersonalData.objects.get(pk=id)
    form = UserForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        form = UserForm()
        return HttpResponseRedirect('/user_details/')
    context = {'form': form}
    return render(request, "user_create.html", context)

def details_view(request, *args, **kwargs):
    users = PersonalData.objects.all()
    return render(request, "user_details.html", {'users': users})
