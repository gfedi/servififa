import json as js

with open("events.json") as events:
    events_dict = js.load(events)

players = set([e["playerId"] for e in events_dict if e["teamId"]
               == 3159 and e["playerId"] != 0])

players_fouls = []

for p in players:
    evs = len([e for e in events_dict if e["playerId"] ==
               p and e["eventName"] == "Foul" and e["matchPeriod"] == "1H"])
    players_fouls.append((p, evs))

ord_players_fouls = sorted(players_fouls, key=lambda x: x[0], reverse=True)

with open("esercizio6.csv", "w") as f:
    f.write(";".join(["playerId", "n_falli_commessi"]))
    f.write("\n")
    for el in ord_players_fouls:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")
