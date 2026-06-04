from django.urls import path
from .views import profile

from . import views

urlpatterns = [
    path("", views.user, name="user"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("user_steam", views.user_steam, name="user_steam"),
]