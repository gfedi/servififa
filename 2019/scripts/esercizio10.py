import json as js

with open("events.json") as events:
    events_dict = js.load(events)

porta = {"x": 100, "y": 50}
shots = [e for e in events_dict if e["subEventName"]
         == "Shot" and e["teamId"] == 3161]
eucl_dist = []

for s in shots:
    shot_pos = s["positions"][0]
    square_dist = pow(shot_pos["x"] - porta["x"], 2) + \
        pow(shot_pos["y"] - porta["y"], 2)
    eucl_dist.append(pow(square_dist, 0.5))

distanza_media = round(sum(eucl_dist)/len(eucl_dist), 4)

with open("esercizio10.csv", "w") as f:
    f.write(";".join(["distanza_media"]))
    f.write("\n")
    f.write(str(distanza_media))
    f.write("\n")
