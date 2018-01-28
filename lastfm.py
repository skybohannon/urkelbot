import urllib.request
import json


def np(user):
    user = user.lower()

    if user == "sky":
        username = "sbohannon"
    elif user == "brett":
        username = "southcore"
        user = "brett"
    elif user == "brandon":
        username = "superprime"

    try:
        with open("lastfm-" + user + "-api.txt", "r") as api_key:
            api_key = api_key.read()
    except FileNotFoundError:
        return "Could not find user {}".format(user)

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
            "title": recent_tracks["recenttracks"]["track"][0]["name"],
        }
        try:
            if recent_tracks["recenttracks"]["track"][0]["@attr"]["nowplaying"] == "true":
                tracks_dict[counter].update({"nowplaying": "true"})
        except KeyError:
            tracks_dict[counter].update({"nowplaying": "false"})

    if tracks_dict[1]["nowplaying"] == "true":
        now_playing = "<b>Now playing</b>:\n" + tracks_dict[1]["artist"] + " - " + tracks_dict[1]["title"]
    else:
        now_playing = "<b>Last played track</b>:\n" + tracks_dict[1]["artist"] + " - " + tracks_dict[1]["title"]

    return now_playing

print(np("sky"))
print(np("invalid_user"))