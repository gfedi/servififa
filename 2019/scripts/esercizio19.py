import json as js

with open("events.json") as events:
    events_dict = js.load(events)

with open("players.json") as events:
    players_dict = js.load(events)

player_duel = []
for p in players_dict:
    duels = len([e for e in events_dict if e["subEventName"] == "Air duel" and
                 e["positions"][0]["y"] <= 75 and e["positions"][0]["y"] >= 25 and
                 e["playerId"] == p["wyId"]])
    if duels:
        player_duel.append((p, duels))


sorted_player_duel = sorted(player_duel, key=lambda x: x[1], reverse=True)[0:3]
sorted_player_solution = [(p[0]["wyId"], p[0]["weight"], p[1])
                          for p in sorted_player_duel]
sorted_final = sorted(sorted_player_solution, key=lambda x: x[0], reverse=True)

with open("esercizio19.csv", "w") as f:
    f.write(";".join(["playerId", "weight", "n_duelli_aerei"]))
    f.write("\n")
    for el in sorted_final:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")
