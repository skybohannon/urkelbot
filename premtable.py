import urllib.request
import json

with open("premkey.txt", "r") as apikey:
    key = apikey.read()

urlData = "http://api.football-api.com/2.0/standings/1204?Authorization=" + key

webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
prem_table = json.loads(data.decode(encoding))

table_dict = {}
game_week = prem_table[0]["round"]

for team in prem_table:
    team_posi = int(team["position"])
    
    table_dict[team_posi] = {
        "name": team["team_name"], 
        "points": team["points"], 
        "form": team["recent_form"], 
        "gd": team["gd"],
        "gs": team["overall_gs"], 
        "ga": team["overall_ga"], 
        "position": team["position"]
    }

print_string = ""
for i in range(len(table_dict)):
    print_string = print_string + "<b>" + str(i+1) + "</b> - " + table_dict[i+1]["name"] + " (" + table_dict[i+1]["points"] + ")\n"

# [:-1] to remove the last \n
print_string = "<b>Premier League GW{}</b>\n\n".format(game_week) + print_string[:-1]
print(print_string)
