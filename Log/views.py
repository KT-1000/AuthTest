from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Don't allow any view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")
