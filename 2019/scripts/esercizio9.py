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


teams = [e["teamId"] for e in events_dict if e["playerId"] != 0]

play_events = []
for t in set(teams):
    evs=0
    maxi=0
    teamtemp=""
    for event in events_dict:
      if event['teamId'] != teamtemp:
         evs=0
      if event['teamId']==t and event['eventName']=="Pass":
        if {"id":1801} in event['tags']:
          evs+=1
          if evs>maxi: maxi=evs
        else:
          evs=0
      teamtemp=event['teamId']
    play_events.append((t, maxi))

ord_play_events = sorted(play_events, key=lambda x: x[0])

with open("esercizio9.csv", "w") as f:
    f.write(";".join(["teamId", "n_pass_azione"]))
    f.write("\n")
    for el in ord_play_events:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")
