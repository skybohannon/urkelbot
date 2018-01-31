import urllib.request
import json


def top10(user):
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

    urlData = "https://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user=" + username + "&api_key=" + api_key + "&format=json"

    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    weekly_chart = json.loads(data.decode(encoding))
    weekly_chart.update(weekly_chart["weeklyartistchart"])

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
    for i in range(0,10):
        top_10 = top_10 + "<b>" + str(i+1) + "</b>. " + top_artists[i]["artist"] + " (<i>" + top_artists[i]["playcount"] + "</i>)\n"

    top_10 = top_10[:-1]
    return top_10

print(top10("brandon"))