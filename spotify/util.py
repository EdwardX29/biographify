import requests 
import math
from collections import OrderedDict
def aboutMeInfo(token):
    url = "https://api.spotify.com/v1/me"
    response = requests.get(url, headers={
        "Authorization": "Bearer " + token
    }).json()

    return response["display_name"]

def getSongs(token, time):
    url = f"https://api.spotify.com/v1/me/top/tracks?time_range={time}"
    headers = {
        "Authorization" : "Bearer " + token
    }
    data = requests.get(url, headers=headers).json()

    songs = []
    duration_total = 0
    for item in data["items"][:10]:
        duration_total += item["duration_ms"]
        songs.append((item["name"], convertTime(duration_total)))
    return songs


def convertTime(msTime):
    minutes = msTime//60_000
    seconds = math.floor((msTime % 60_000)/1000)
    secString = "0" + str(seconds) if seconds < 10 else str(seconds)
    return f"{minutes}:{secString}"