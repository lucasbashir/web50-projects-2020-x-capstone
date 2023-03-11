from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("new_alert", views.new_alert, name="new_alert"),
    path("all_alerts", views.all_alerts, name="all_alerts"),



]
