import urllib.request
import json
from sortedcontainers import SortedDict

with open("premkey.txt", "r") as apikey:
    key = apikey.read()

urlData = "http://api.football-api.com/2.0/standings/1204?Authorization=" + key
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
prem_table = json.loads(data.decode(encoding))

table_dict = SortedDict({1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}, 9:{}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}})
game_week = prem_table[0]["round"]

for team in prem_table:
    team_posi = int(team["position"])
    table_dict[team_posi]["name"] = team["team_name"]
    table_dict[team_posi]["points"] = team["points"]
    table_dict[team_posi]["form"] = team["recent_form"]
    table_dict[team_posi]["gd"] = team["gd"]
    table_dict[team_posi]["gs"] = team["overall_gs"]
    table_dict[team_posi]["ga"] = team["overall_ga"]
    table_dict[team_posi]["position"] = team["position"]

count = 1
print_string = ""
while count <= 20:
    print_string = print_string + "<b>" + str(count) + "</b> - " + table_dict[count]["name"] + " (" + table_dict[count]["points"] + ")\n"
    count += 1
print_string = "<b>Premier League GW{}</b>\n\n".format(game_week) + print_string
print(print_string)