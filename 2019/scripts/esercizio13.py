import json as js

with open("events.json") as events:
    events_dict = js.load(events)

fouls = [e for e in events_dict if e["subEventName"] == "Foul"]
yellow = [e for e in events_dict if ({"id":1702} in e["tags"])]

print(len(yellow))

teams = [e["teamId"] for e in events_dict if e["playerId"] != 0]

team_events = []
for t in set(teams):
    evsF = len([e for e in fouls if e["teamId"] == t and e["playerId"] != 0 ])
    evsY = len([e for e in yellow if e["teamId"] != t and e["playerId"] != 0 ])
    team_events.append((t, str(round(evsF/evsY,4))))

ord_team_events = sorted(team_events, key=lambda x: x[0])

with open("esercizio13.csv", "w") as f:
    f.write(";".join(["teamId", "ratio"]))
    f.write("\n")
    for el in ord_team_events:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")

