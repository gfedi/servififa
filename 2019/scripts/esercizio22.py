import json as js

with open("events.json") as events:
    events_dict = js.load(events)

n_spazzate = len([e for e in events_dict if e["subEventName"] == "Clearance" and
                  e["positions"][0]["x"] >= 0 and e["positions"][0]["x"] <= 25])


with open("esercizio22.csv", "w") as f:
    f.write(";".join(["n_spazzate"]))
    f.write("\n")
    f.write(str(n_spazzate))
    f.write("\n")
