import urllib.request
import json
import os
import aiohttp
import io
import asyncio
import re

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
    recent_tracks.update(recent_tracks["recenttracks"])
    tracks_dict = {}
    counter = 1

    print(recent_tracks)

    for track in recent_tracks:
        tracks_dict[counter] = {
            "artist": recent_tracks["track"][0]["artist"]["#text"],
            "title": recent_tracks["track"][0]["name"],
            "album_art": recent_tracks["track"][0]["image"][0]["#text"]
        }
        try:
            if recent_tracks["recenttracks"]["track"][0]["@attr"]["nowplaying"] == "true":
                tracks_dict[counter].update({"nowplaying": "true"})
        except KeyError:
            tracks_dict[counter].update({"nowplaying": "false"})

    if tracks_dict[1]["nowplaying"] == "true":
        now_playing = "<b>{}'s Now Playing</b>:\n".format(user.capitalize()) + tracks_dict[1]["artist"] + " - " + tracks_dict[1]["title"]
    else:
        now_playing = "<b>{}'s Last Played Track</b>:\n".format(user.capitalize()) + tracks_dict[1]["artist"] + " - " + tracks_dict[1]["title"]

    print(tracks_dict[1]["album_art"])


    image = tracks_dict[1]["album_art"]
    imagelink = tracks_dict[1]["album_art"]
    filename = os.path.basename(imagelink)
    r = yield from aiohttp.request('get',imagelink)
    raw = yield from r.read()
    image_data = io.BytesIO(raw)
    image_id = yield from bot._client.upload_image(image_data, filename=filename)
    yield from bot.coro_send_message(event.conv.id_, None, image_id=image_id)

    
    return now_playing

print(np("sky"))
print(np("invalid_user"))