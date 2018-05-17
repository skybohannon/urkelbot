import urllib.request
import json

def top10(user):
    user = user.lower()

    with open("lastfm.json", "r") as f:
        usernames = json.load(f)

    try:
        if user in usernames:
            username = usernames[user]["username"]
            api_key = usernames[user]["key"]

        urlData = "https://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user=" + username + "&api_key=" + api_key + "&format=json"

        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        weekly_chart = json.loads(data.decode(encoding))
        weekly_chart.update(weekly_chart["weeklyartistchart"])
        track_art = chart["track"][0]["image"][3:4][0]["#text"]
        top_artists = {}
        counter = 0
        for item in weekly_chart["artist"]:
            top_artists[counter] = {
                "artist": item["name"],
                "playcount": item["playcount"],
                "rank": item["@attr"]["rank"]
            }
            counter += 1

        top_10 = "<b>{}'s Top 10 Artists of the Week</b>:\n\n".format(user.capitalize())
        try:
            for i in range(0, 10):
                top_10 = top_10 + "<b>" + str(i + 1) + "</b>. " + top_artists[i]["artist"] + " (<i>" + top_artists[i][
                "playcount"] + "</i>)\n"

            top_10 = top_10[:-1]
        except KeyError:
            top_10 = "{}, you have less than 10 artists. Listen to some more music already you bum!".format(user.capitalize())

        return top_10
    except UnboundLocalError:
        top_10 = "Could not find user {}".format(user)

print(top10("sky"))