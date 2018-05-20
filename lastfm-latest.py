import urllib.request, json, os, aiohttp, io


def latest(user):
    user = user.lower()

    with open("lastfm.json", "r") as f:
        usernames = json.load(f)

    try:
        if user in usernames:
            username = usernames[user]["username"]
            api_key = usernames[user]["key"]

        urlData = "https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + username + "&api_key=" + api_key + "&limit=10&format=json"

        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        recent_tracks = json.loads(data.decode(encoding))
        recent_tracks.update(recent_tracks["recenttracks"])

        track_art = recent_tracks["track"][0]["image"][3:4]
        track_art = track_art[0]["#text"]

        counter = 0
        for item in recent_tracks["track"]:
            recent_tracks[counter] = {
                "track": item["name"],
                "artist": item["artist"]["#text"]
            }
            counter += 1

        top_10 = "<b>{}'s Recent Tracks</b>\n\n".format(user.capitalize())

        #try:
        #    filename = os.path.basename(track_art)
        #     r = yield from aiohttp.request('get', track_art)
        #     raw = yield from r.read()
        #     image_data = io.BytesIO(raw)
        #     image_id = yield from bot._client.upload_image(image_data, filename=filename)
        #     yield from bot.coro_send_message(event.conv.id_, None, image_id=image_id)
        #except ValueError:
        #    pass

        try:
            for i in range(0, 10):
                top_10 = top_10 + "<b>" + str(i + 1) + "</b>. " + str(track_art) + [i]["artist"] + " - " + recent_tracks[i]["track"] + "\n"

            return top_10[:-1]

        except KeyError:
            return

    except UnboundLocalError:
        return "\'{}\' is not in my user database.".format(user)

print(latest("sky"))