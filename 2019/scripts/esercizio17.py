import json as js

csv_headers = ['tempo', 'momento', 'distanza']

with open("events.json") as events:
    events_dict = js.load(events)

with open("players.json") as events:
    players_dict = js.load(events)

player_intercept = []
for p in players_dict:
    intercept = len([e for e in events_dict if e["teamId"] == 3159 and {
                    "id": 1401} in e["tags"] and e["playerId"] == p["wyId"]])
    if intercept:
        player_intercept.append((p, intercept))

sorted_player_intercept = sorted(
    player_intercept, key=lambda x: x[1], reverse=True)[0:3]
sorted_player_solution = [(p[0]["wyId"], p[0]["role"]["name"], p[1])
                          for p in sorted_player_intercept]

with open("esercizio17.csv", "w") as f:
    f.write(";".join(["playerId", "role", "n_intercetti"]))
    f.write("\n")
    for el in sorted_player_solution:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")
