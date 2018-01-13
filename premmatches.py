import urllib.request
import json
from datetime import datetime
import pytz

with open("premkey.txt", "r") as apikey:
    key = apikey.read()


# Convert time to normal time instead of military time, change time zone to Central
def time_convert(time):

    mil_time = time
    hours, minutes = mil_time.split(":")
    hours, minutes = int(hours) - 6, int(minutes)
    am_pm = "AM"

    if hours > 12:
        am_pm = "PM"
        hours -= 12
    return "{}:{:02d}".format(hours, minutes) + am_pm


# Check events for goals, then return goals
def get_events(l):
    events = ""
    event_list = []
    for i in range(len(l)):
        if l[i]["type"] == "goal":
            player = l[i]["player"]
            minute = l[i]["minute"]
            single_event = player + " " + minute + "'"
            event_list.append(single_event)
            events = ", ".join(event_list)
            i += 1
    return events


tz = pytz.timezone('America/Chicago')
current_date = datetime.now(tz=tz).strftime("%d.%m.%Y")

urlData = "http://api.football-api.com/2.0/matches?comp_id=1204&match_date=" + current_date + "&Authorization=" + key

webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
matches = json.loads(data.decode(encoding))

matches_dict = {}
matches_date = matches[0]["formatted_date"]
matches_date = datetime.strptime(matches_date, '%d.%m.%Y').strftime('%m/%d/%Y')

count = 1
for match in matches:
    match_id = count
    matches_dict[match_id] = {
        "home": match["localteam_name"],
        "visitor": match["visitorteam_name"],
        "home_score": match["localteam_score"],
        "visitor_score": match["visitorteam_score"],
        "status": match["status"],
        "events": match["events"]
    }

    try:
        matches_dict[match_id]["status"] = str(int(matches_dict[match_id]["status"])) + "'"
    except ValueError:
        matches_dict[match_id]["status"] = matches_dict[match_id]["status"]

    if len(matches_dict[match_id]["status"]) == 5:
        matches_dict[match_id]["status"] = time_convert(matches_dict[match_id]["status"])

    count += 1

print_string = ""
for i in range(len(matches_dict)):
    print_string = print_string + matches_dict[i+1]["home"] + " <b>" + matches_dict[i+1]["home_score"] + " - " + matches_dict[i+1]["visitor_score"] + "</b> " + matches_dict[i+1]["visitor"] + " " + matches_dict[i+1]["status"] + "\n"
    if len(get_events(matches_dict[i + 1]["events"])) > 0:
        print_string = print_string + "<i>(" + get_events(matches_dict[i + 1]["events"]) + ")</i>\n\n"
    else:
        print_string = print_string + "\n"

print_string = "<b>Match scores for " + matches_date + "</b>\n\n" + print_string[:-1]
print(print_string)
