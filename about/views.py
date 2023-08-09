from django.shortcuts import render
from .models import About


def about_me(request, *args, **kwargs):
    """
    Renders the view for the about.html template
    """

    about = About.objects.all().first()

    return render(
        request,
        "about.html",
        {
            "about": about
        },
    )
