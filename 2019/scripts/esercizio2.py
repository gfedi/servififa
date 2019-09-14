import json as js

with open("events.json") as events:
    events_dict = js.load(events)


teams = [e["teamId"] for e in events_dict if e["playerId"] != 0]

team_events = []
for t in set(teams):
    evs = len([e for e in events_dict if e["teamId"]
               == t and e["playerId"] != 0])
    team_events.append((t, evs))

ord_team_events = sorted(team_events, key=lambda x: x[0])

with open("esercizio2.csv", "w") as f:
    f.write(";".join(["teamId", "n_events"]))
    f.write("\n")
    for el in ord_team_events:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")
