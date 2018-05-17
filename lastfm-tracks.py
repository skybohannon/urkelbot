import urllib.request
import json

def tracks(type, user):
    user = user.lower()

    with open("lastfm.json", "r") as f:
        usernames = json.load(f)

    try:
        if user in usernames:
            username = usernames[user]["username"]
            api_key = usernames[user]["key"]

        if type == "week":
            urlData = "https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=" + username + "&api_key=" + api_key + "&period=7day&format=json"
        elif type == "month":
            urlData = "https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=" + username + "&api_key=" + api_key + "&period=1month&format=json"
        elif type == "alltime":
            urlData = "https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=" + username + "&api_key=" + api_key + "&period=overall&format=json"
        elif type == "year":
            urlData = "https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=" + username + "&api_key=" + api_key + "&period=12month&format=json"

        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        chart = json.loads(data.decode(encoding))

        if type == "week":
            chart.update(chart["toptracks"])
            top_10 = "<b>{}'s Top 10 Tracks of the Week</b>\n\n".format(user.capitalize())
        elif type == "month":
            chart.update(chart["toptracks"])
            top_10 = "<b>{}'s Top 10 Tracks of the Month</b>\n\n".format(user.capitalize())
        elif type == "year":
            chart.update(chart["toptracks"])
            top_10 = "<b>{}'s Top 10 Tracks of The Past Year</b>\n\n".format(user.capitalize())
        elif type == "alltime":
            chart.update(chart["toptracks"])
            top_10 = "<b>{}'s Top 10 Tracks of All Time</b>\n\n".format(user.capitalize())

        track_art = chart["track"][0]["image"][3:4][0]["#text"]

        top_tracks = {}
        counter = 0
        for item in chart["track"]:
            top_tracks[counter] = {
                "track": item["name"],
                "artist": item["artist"]["name"],
                "playcount": item["playcount"],
                "rank": item["@attr"]["rank"]
            }
            counter += 1



        try:
            for i in range(0, 10):
                top_10 = top_10 + "<b>" + str(i + 1) + "</b>. " +top_tracks[i]["artist"] + " - " + top_tracks[i]["track"] + " (<i>" + top_tracks[i][
                "playcount"] + "</i>)\n"

            return top_10[:-1]

        except KeyError:
            return

    except UnboundLocalError:
        return "\'{}\' is not in my user database.".format(user)

print(tracks("week","sky"))