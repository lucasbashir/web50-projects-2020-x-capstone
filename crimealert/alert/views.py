from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *
import requests
import json
import re
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync 


def index(request):
   return render(request, "index.html")

def all_alerts(request):
    alert = Alert.objects.all()
    return render(request, "all_alerts.html", {
        "alert": alert
    })

def new_post_alert(request):
    # your logic to create a new post

    # send message to WebSocket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'new_post_alert', {
            'type': 'alert.message',
            'message': 'A new post has been created!'
        }
    )

    return HttpResponse('New post created')

def new_alert(request):
    if request.method == "GET":
        return render(request, "new_alert.html")
    else:
        content = request.POST["content"]
        location = request.POST["location"] 
        longitude = request.POST["longitude"]
        latitude = request.POST["latitude"] 
        current_user = request.user 

        longitude_pattern = re.compile(r'^[-+]?(180(\.0+)?|(1[0-7]\d|[1-9]?\d)(\.\d+)?)$')
        latitude_pattern = re.compile(r'^[-+]?(90(\.0+)?|[1-8]?\d(\.\d+)?)$')

        if longitude_pattern.match(longitude) and latitude_pattern.match(latitude):

            new_alert = Alert(content=content, location=location, longitude=longitude, latitude=latitude, user=current_user)
            new_alert.save()   
            return HttpResponseRedirect(reverse("all_alerts"))
        else:
            # Add a proper error message
            return HttpResponse("Invalid longitude or latitude. Please provide a valid longitude and latitude.")
        


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

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")