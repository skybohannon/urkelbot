import urllib.request
import json

urlData = "http://api.football-api.com/2.0/standings/1204?Authorization=565ec012251f932ea4000001fa542ae9d994470e73fdb314a8a56d76"
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

for i in range(len(table_dict)):
    print_string = "<b>" + str(i+1) + "</b> - " + table_dict[i+1]["name"] + " (" + table_dict[i+1]["points"] + ")\n"
    print_string = "<b>Premier League GW{}</b>\n\n".format(game_week) + print_string
    print(print_string)
