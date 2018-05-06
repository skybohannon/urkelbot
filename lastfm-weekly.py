import urllib.request
import json


def weekly(type, user):
    user = user.lower()
    type = type.lower()

    with open("lastfm.json", "r") as f:
        usernames = json.load(f)

    def getcharts(type, user):
        global weekly_chart
        urlData = "https://ws.audioscrobbler.com/2.0/?method=user.getyearly" + type + "chart&user=" + username + "&api_key=" + api_key + "&format=json"
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        weekly_chart = json.loads(data.decode(encoding))
        weekly_chart.update(weekly_chart["weekly" + type + "chart"])
        return weekly_chart


    try:
        if user in usernames:
            username = usernames[user]["username"]
            api_key = usernames[user]["key"]

        if type == "artists":
            type = "artist"
        if type == "tracks":
            type = "track"
        if type == "albums":
            type = "album"

        if type == "artist" or type == "album" or type == "track":
            try:
                getcharts(type, user)
            except NameError:
                return "Could not find user '{}'".format(user)

        tops = {}
        counter = 0
        for item in weekly_chart[type]:
            tops[counter] = {
                "artist": item["name"],
                "playcount": item["playcount"],
                "rank": item["@attr"]["rank"]
            }
            counter += 1

        top_10 = "<b>{}'s Top 10 " + type.capitalize() + "s of the Week</b>:\n\n".format(user.capitalize())
        for i in range(0,10):
            top_10 = top_10 + "<b>" + str(i+1) + "</b>. " + tops[i]["artist"] + " (<i>" + tops[i]["playcount"] + "</i>)\n"

        return top_10[:-1]

    except UnboundLocalError:
        return("Could not find user {}".format(user))

print(weekly("tracks","sky"))