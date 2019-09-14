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

total_foul=0
play_events = []
for t in set(players):
    evs = len([e for e in events_dict if e["teamId"]
               == Juve["wyId"] and e["playerId"] != 0 and e["playerId"]==t and e['eventName']=="Foul" and e['matchPeriod']=="2H"])
    total_foul+=evs
    play_events.append((t, evs))

with open("esercizio5.csv", "w") as f:
    f.write(";".join(["n_falli_subiti"]))
    f.write("\n")
    f.write(str(total_foul))
    f.write("\n")
