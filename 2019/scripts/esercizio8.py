import json as js

with open("events.json") as events:
    events_dict = js.load(events)

n_dribbling = 0
for ev, ev_p1, ev_p2 in zip(events_dict, events_dict[1:], events_dict[2:]):
    if ev["subEventName"] == "Ground attacking duel" and {"id": 1801} in ev["tags"]:
        if ev_p1["subEventName"] == "Shot":
            n_dribbling += 1
        elif ev_p1["subEventName"] == "Ground defending duel" and ev_p2["subEventName"] == "Shot":
            n_dribbling += 1

with open("esercizio8.csv", "w") as f:
    f.write(";".join(["n_dribbling"]))
    f.write("\n")
    f.write(str(n_dribbling))
