from django.shortcuts import render


def details_view(request, *args, **kwargs):
    users = {
        "arthur": "panther",
        "itamar": "lo chef"
    }
    return render(request, "user_details.html", users)
