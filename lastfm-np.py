import urllib.request, json, os, aiohttp, io

def np(user):
    user = user.lower()

    if user == "sky":
        username = "sbohannon"
    elif user == "brett":
        username = "southcore"
    elif user == "brandon":
        username = "superprime"

    try:
        with open("lastfm-" + user + "-api.txt", "r") as api_key:
            api_key = api_key.read()

        urlData = "https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + username + "&api_key=" + api_key + "&format=json"

        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        recent_tracks = json.loads(data.decode(encoding))
        recent_tracks.update(recent_tracks["recenttracks"])

        track_artist = recent_tracks["track"][0]["artist"]["#text"]
        track_title = recent_tracks["track"][0]["name"]
        track_art = recent_tracks["track"][0]["image"][3:4]
        track_art = track_art[0]["#text"]
        now_playing = "false"

        try:
            if recent_tracks["track"][0]["@attr"]["nowplaying"] == "true":
                now_playing = "true"
        except KeyError:
            now_playing = "false"

        if now_playing == "true":
            now_playing = "<b>{}'s Now Playing</b>:\n".format(user.capitalize()) + track_artist + " - " + track_title
        else:
            now_playing = "<b>{}'s Last Played Track</b>:\n".format(
                user.capitalize()) + track_artist + " - " + track_title

        try:
            filename = os.path.basename(track_art)
            r = yield from aiohttp.request('get', track_art)
            raw = yield from r.read()
            image_data = io.BytesIO(raw)
            image_id = yield from bot._client.upload_image(image_data, filename=filename)
            yield from bot.coro_send_message(event.conv.id_, None, image_id=image_id)
        except ValueError:
            pass

    except FileNotFoundError:
        return "Could not find user {}".format(user)

    return now_playing

print(np("sky"))
print(np("invalid_user"))