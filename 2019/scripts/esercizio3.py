import json as js

with open("events.json") as events:
    events_dict = js.load(events)

with open("teams.json") as teams:
    teams_dict = js.load(teams)

Inter={}
Juve={}

for team in teams_dict:
  if team['name']=="Internazionale": Inter=team
  if team['name']=="Juventus": Juve=team


players = [e["playerId"] for e in events_dict if e["playerId"] != 0]

play_events = []
for t in set(players):
    evs = len([e for e in events_dict if e["teamId"]
               == Inter["wyId"] and e["playerId"] != 0 and e["playerId"]==t and e['eventName']=="Pass"])
    play_events.append((t, evs))

ord_play_events = sorted(play_events, key=lambda x: x[0])

with open("esercizio3.csv", "w") as f:
    f.write(";".join(["playerId", "n_pass"]))
    f.write("\n")
    for el in ord_play_events:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")
