from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def user(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users_login/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("user"))
        else:
            return render(request, "users_login/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "users_login/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users_login/login.html", {
        "message": "Logged out."
    })

@login_required
def profile(request):
    return render(request, "user_steam.html")