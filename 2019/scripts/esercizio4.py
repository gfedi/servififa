import json as js

with open("events.json") as events:
    events_dict = js.load(events)

players = set([e["playerId"] for e in events_dict if e["teamId"]
               == 3159 and e["playerId"] != 0])

players_simplepass = []

for p in players:
    evs = len([e for e in events_dict if e["playerId"] ==
               p and e["subEventName"] == "Simple pass"])
    players_simplepass.append((p, evs))

ord_players_simplepass = sorted(
    players_simplepass, key=lambda x: x[0], reverse=True)

with open("esercizio4.csv", "w") as f:
    f.write(";".join(["playerId", "n_simple_pass"]))
    f.write("\n")
    for el in ord_players_simplepass:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")
