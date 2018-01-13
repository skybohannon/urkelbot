match = {"id":"2213136",
         "comp_id":"1204",
         "formatted_date":"13.01.2018",
         "season":"2017\/2018",
         "week":"23",
         "venue":"The Hawthorns (West Bromwich)",
         "venue_id":"17470",
         "venue_city":"West Bromwich",
         "status":"40",
         "timer":"40",
         "time":"15:00",
         "localteam_id":"9426",
         "localteam_name":"West Brom",
         "localteam_score":"1",
         "visitorteam_id":"9065",
         "visitorteam_name":"Brighton",
         "visitorteam_score":"0",
         "ht_score":"[1-0]",
         "ft_score":"[-]",

         "events":[{"id":"23770381",
                    "type":"goal",
                    "minute":"4",
                    "extra_min":"",
                    "team":"localteam",
                    "player":"J. Evans",
                    "player_id":"20687",
                    "assist":"J. Rodriguez",
                    "assist_id":"15915",
                    "result":"[1-0]"},
                   {"id": "23770381",
                    "type": "goal",
                    "minute": "4",
                    "extra_min": "",
                    "team": "localteam",
                    "player": "B. Doo",
                    "player_id": "20687",
                    "assist": "J. Rodriguez",
                    "assist_id": "15915",
                    "result": "[1-0]"}
                   ]}

event_list = []
for i in range(len(match["events"])):
    player = match["events"][i]["player"]
    minute = match["events"][i]["minute"]
    single_event = player + " " + minute + "'"
    event_list.append(single_event)
    events = ", ".join(event_list)
    i += 1

print(events)