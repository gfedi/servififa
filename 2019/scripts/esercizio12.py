import json as js

with open("events.json") as events:
    events_dict = js.load(events)

with open("matches.json") as events:
    matches_dict = js.load(events)

match = [m for m in matches_dict if m["wyId"] == 2576302][0]

players_sub = [el["playerIn"] for el in match["teamsData"]["3159"]["formation"]["substitutions"]] + \
              [el["playerIn"] for el in match["teamsData"]
                  ["3161"]["formation"]["substitutions"]]

players_corner = []

for p in players_sub:
    corner_kicks = len(
        [el for el in events_dict if el["subEventName"] == "Corner" and el["playerId"] == p])
    players_corner.append((p, corner_kicks))

ord_players_corner = sorted(players_corner, key=lambda x: x[0], reverse=True)

with open("esercizio12.csv", "w") as f:
    f.write(";".join(["playerId", "corner_kicks"]))
    f.write("\n")
    for el in ord_players_corner:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")
