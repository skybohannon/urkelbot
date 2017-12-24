import urllib.request
import json

urlData = "http://api.football-api.com/2.0/standings/1204?Authorization=565ec012251f932ea4000001fa542ae9d994470e73fdb314a8a56d76"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
prem_table = json.loads(data.decode(encoding))

table_dict = {"1":{}, "2":{}, "3":{}, "4":{}, "5":{}, "6":{}, "7":{}, "8":{}, "9":{}, "10":{}, "11":{}, "12":{}, "13":{}, "14":{}, "15":{}, "16":{}, "17":{}, "18":{}, "19":{}, "20":{}}
game_week = prem_table[0]["round"]

for team in prem_table:
    team_posi = team["position"]
    table_dict[team_posi]["name"] = team["team_name"]
    table_dict[team_posi]["points"] = team["points"]
    table_dict[team_posi]["form"] = team["recent_form"]
    table_dict[team_posi]["gd"] = team["gd"]
    table_dict[team_posi]["gs"] = team["overall_gs"]
    table_dict[team_posi]["ga"] = team["overall_ga"]
    table_dict[team_posi]["position"] = team["position"]

print("Premier League GW {}".format(game_week))
print(table_dict)
