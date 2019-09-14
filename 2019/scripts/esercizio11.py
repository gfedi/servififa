import json as js

with open("events.json") as events:
    events_dict = js.load(events)

shots = [e for e in events_dict if e["subEventName"]
         == "Ground defending duel" and e["teamId"] == 3159]

eucl_distx = []
eucl_disty = []

for s in shots:
    shot_pos = s["positions"][0]
    eucl_distx.append(shot_pos["x"])
    eucl_disty.append(shot_pos["y"])

distanza_mediax = round(sum(eucl_distx)/len(eucl_distx), 4)
distanza_mediay = round(sum(eucl_disty)/len(eucl_disty), 4)

with open("esercizio11.csv", "w") as f:
    f.write(";".join(["p_tackle_x","p_tackle_y"]))
    f.write("\n")
    f.write(str(distanza_mediax)+";"+str(distanza_mediay))
    f.write("\n")

