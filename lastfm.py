import urllib.request
import json


def nowplaying(user):
    user = user.lower()
    with open("lastfm-" + user + "-api.txt", "r") as api_key:
        api_key = api_key.read()

    with open("lastfm-" + user + "-secret.txt", "r") as api_secret:
        api_secret = api_secret.read()

    if user == "sky":
        username = "sbohannon"
    elif user == "brett":
        username = "auchief"
    elif user == "brandon":
        username = "superprime"

    urlData = "https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + username + "&api_key=" + api_key +"&format=json"

    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    recent_tracks = json.loads(data.decode(encoding))

    tracks_dict = {}
    counter = 1
    for track in recent_tracks:
        tracks_dict[counter] = {
            "artist": recent_tracks["recenttracks"]["track"][0]["artist"]["#text"],
            "title": recent_tracks["recenttracks"]["track"][0]["name"]
        }
        counter += 1

    nowplaying = "<b>Now playing</b>:\n" + tracks_dict[1]["artist"] + " - " + tracks_dict[1]["title"]
    return nowplaying

print(nowplaying("sky"))
