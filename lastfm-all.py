import urllib.request
import json

def top10(type, user):
    user = user.lower()

    with open("lastfm.json", "r") as f:
        usernames = json.load(f)

    try:
        if user in usernames:
            username = usernames[user]["username"]
            api_key = usernames[user]["key"]

        if type == "week":
            urlData = "https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=" + username + "&api_key=" + api_key + "&period=7day&format=json"
        elif type == "month":
            urlData = "https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=" + username + "&api_key=" + api_key + "&period=1month&format=json"
        elif type == "alltime":
            urlData = "https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=" + username + "&api_key=" + api_key + "&period=overall&format=json"
        elif type == "year":
            urlData = "https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=" + username + "&api_key=" + api_key + "&period=12month&format=json"

        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        chart = json.loads(data.decode(encoding))

        if type == "week":
            chart.update(chart["topartists"])
            top_10 = "<b>{}'s Top 10 Artists of the Week</b>\n\n".format(user.capitalize())
            track_art = chart["artist"][0]["image"][3:4][0]["#text"]
        elif type == "month":
            chart.update(chart["topartists"])
            top_10 = "<b>{}'s Top 10 Artists of the Month</b>\n\n".format(user.capitalize())
            track_art = chart["artist"][0]["image"][3:4][0]["#text"]
        elif type == "alltime":
            chart.update(chart["topartists"])
            top_10 = "<b>{}'s Top 10 Artists of All Time</b>\n\n".format(user.capitalize())
            track_art = chart["artist"][0]["image"][3:4][0]["#text"]
        elif type == "year":
            chart.update(chart["topartists"])
            top_10 = "<b>{}'s Top 10 Artists of The Past Year</b>\n\n".format(user.capitalize())
            track_art = chart["artist"][0]["image"][3:4][0]["#text"]


        top_artists = {}
        counter = 0
        for item in chart["artist"]:
            top_artists[counter] = {
                "artist": item["name"],
                "playcount": item["playcount"],
                "rank": item["@attr"]["rank"]
            }
            counter += 1

        try:
            for i in range(0, 10):
                top_10 = top_10 + "<b>" + str(i + 1) + "</b>. " + top_artists[i]["artist"] + " (<i>" + top_artists[i][
                "playcount"] + "</i>)\n"

            top_10 = top_10[:-1]

            return top_10

        except KeyError:
            return "I think you need to listen to more music! You have less than 10 artists listened to in the past week."

    except UnboundLocalError:
        top_10 = "Could not find user {}".format(user)

print(top10("week","sky"))