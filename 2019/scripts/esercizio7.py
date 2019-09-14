import json as js

with open("events.json") as events:
    events_dict = js.load(events)

with open("teams.json") as teams:
    teams_dict = js.load(teams)

with open("players.json") as playersfile:
    players_dict = js.load(playersfile)

Inter={}
Juve={}
for team in teams_dict:
  if team['name']=="Internazionale": Inter=team
  if team['name']=="Juventus": Juve=team


players = [e["playerId"] for e in events_dict if e["playerId"] != 0]

play_events = []
for t in set(players):
  if [player["role"]["name"] for player in players_dict if player["wyId"]==t] == ["Forward"]: 
    evs = len([e for e in events_dict if e["playerId"] != 0 and 
                                         e["playerId"]==t and 
                                         e['subEventName']=='Ground attacking duel' and
                                         [player["role"]["name"] for player in players_dict if player["wyId"]==e["playerId"]] == ["Forward"] and
                                         e['matchPeriod']=='2H' and
                                         e['eventSec']>=1200 and
                                         ({"id":1802} in e['tags'])
                                          ])
    #print(t,evs)
    play_events.append((t, evs))

ord_play_events = sorted(play_events, key=lambda x: x[0])

with open("esercizio7.csv", "w") as f:
    f.write(";".join(["playerId", "n_dribbling"]))
    f.write("\n")
    for el in ord_play_events:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")
