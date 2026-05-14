from django.shortcuts import redirect, render
from django.contrib.auth.forms import *
from . models import *
from . filters import GameFilter

# Create your views here.


def index(request):
    return render(request, "videogames_100/index.html", {
        "games": Game.objects.all()
    })
    


# def games(request):
#     return render(request, "videogames_100/games.html", {
#         "games": Game.objects.all()
#     })


def games(request):
    games = Game.objects.all()
    game_filter = GameFilter(request.GET, queryset=games)
    return render(request, "videogames_100/games.html", {
        "filter": game_filter
    })

