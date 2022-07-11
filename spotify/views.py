from django.shortcuts import render, redirect
from django.http import HttpResponse
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
import requests
from .util import aboutMeInfo, getSongs, convertTime
import math
# Create your views here.

def index(request):
    if request.method != "POST":
        return render(request, "spotify/index.html")
    else:
        username = request.POST.get("name")
        request.session["username"] = username

        return redirect("spotify:login")

def login(request):
    return render(request, "spotify/login.html")
def authorize(request):
    client_id = CLIENT_ID 
    url = "https://accounts.spotify.com/authorize"
    scopes = "user-top-read"

    params = {
        "client_id" : client_id, 
        "response_type" : "code",
        "redirect_uri" : REDIRECT_URI,
        "scope" : scopes,
    }
    response = requests.get(url, params = params)
    return redirect(response.url)


def callback(request):
    code = request.GET.get("code")
    
    response = requests.post(
        "https://accounts.spotify.com/api/token", 
        data= {
            "grant_type" : "authorization_code",
            "code" : code,
            "redirect_uri" : REDIRECT_URI,
            "client_id" : CLIENT_ID,
            "client_secret" : CLIENT_SECRET,
        }
    ).json()

    access_token = response.get("access_token")
    token_type = response.get("token_type")
    scope = response.get("scope")
    expires_in = response.get("expires_in")
    refresh_token = response.get("refresh_token")

    request.session["token"] = access_token
    return render(request,"spotify/callback.html")

def short_term(request):
    try:
        token = request.session["token"]
        songs = getSongs(token, "short_term")
    except:
        return redirect("spotify:index")
    # username = aboutMeInfo(token)
    username = request.session["username"]
    context = {
        "songs" : songs,
        "username" : username,
    }
    return render(request, "spotify/short_term.html", context=context)
    

def medium_term(request):
    try:
        token = request.session["token"]
        songs = getSongs(token, "medium_term")
    except:
        return redirect("spotify:index")
    username = request.session["username"]
    context = {
        "songs" : songs,
        "username" : username
    }
    return render(request, "spotify/medium_term.html", context=context)
    

def long_term(request):
    
    try:
        token = request.session["token"]
        songs  = getSongs(token, "long_term")
    except:
        return redirect("spotify:index")
    username = request.session["username"]
    context = {
        "songs" : songs,
        "username" : username
    }
    return render(request, "spotify/long_term.html", context=context)