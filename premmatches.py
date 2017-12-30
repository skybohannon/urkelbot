import urllib.request
import json
import datetime

with open("premkey.txt", "r") as apikey:
    key = apikey.read()

urlData = "http://api.football-api.com/2.0/matches?comp_id=1204&Authorization=" + key

webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
matches = json.loads(data.decode(encoding))

matches_dict = {}
matches_date = matches[0]["formatted_date"]
matches_date = datetime.datetime.strptime(matches_date, '%d.%m.%Y').strftime('%m/%d/%Y')

count = 1
for match in matches:
    match_id = count
    matches_dict[match_id] = {
        "home": match["localteam_name"],
        "visitor": match["visitorteam_name"],
        "home_score": match["localteam_score"],
        "visitor_score": match["visitorteam_score"],
        "status": match["status"],
    }
    try:
        matches_dict[match_id]["status"] = str(int(matches_dict[match_id]["status"])) + "'"
    except ValueError:
        matches_dict[match_id]["status"] = matches_dict[match_id]["status"]
    count += 1

print_string = ""
for i in range(len(matches_dict)):
    print_string = print_string + matches_dict[i+1]["home"] + " <b>" + matches_dict[i+1]["home_score"] + " - " + matches_dict[i+1]["visitor_score"] + "</b> " + matches_dict[i+1]["visitor"] + " " + matches_dict[i+1]["status"] + "\n"

print_string = "<b>Match scores for " + matches_date + "</b>\n\n" + print_string[:-1]
print(print_string)
