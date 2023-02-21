from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *

import json
import re


from django.core.paginator import Paginator



def index(request):
   return render(request, "index.html")


def all_alerts(request):
    alert = Alert.objects.all().order_by("id").reverse()
    paginator = Paginator(alert, 10) # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_post = paginator.get_page(page_number)

    return render(request, "all_alerts.html", {
        "alert": alert,
        "page_post": page_post
    })

def new_alert(request):
    if request.method == "GET":
        return render(request, "new_alert.html")
    else:
        content = request.POST["content"]
        state = request.POST["state"]
        lga = request.POST["lga"]
        category = request.POST["category"]
        current_user = request.user

        # Create a new alert
        new_alert = Alert(content=content, state=state, lga=lga, user=current_user, category=category)
        new_alert.save()
        return HttpResponseRedirect(reverse("all_alerts"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
            "message": "Invalid username and/or password"
        })

    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match"
            })

        if not (username and email and password):
            return render(request, "register.html", {
                "message": "Please fill in all fields."
            })

        # Check if the email address already exists in the database
        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "message": "Email already taken."
            })

        # Create a new user account if the email is unique
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError as e:
            if 'unique constraint' in str(e).lower() and 'username' in str(e).lower():
                return render(request, "register.html", {
                    "message": "Username already taken."
                })
    else:
        return render(request, "register.html")
