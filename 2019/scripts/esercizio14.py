import json as js

with open("events.json") as events:
    events_dict = js.load(events)

diff_time = []

ev_1h = [e for e in events_dict if e["matchPeriod"] == "1H"]
ev_2h = [e for e in events_dict if e["matchPeriod"] == "2H"]

for ev, ev_1 in zip(ev_1h, ev_1h[1:]):
    diff_time.append(ev_1["eventSec"] - ev["eventSec"])

for ev, ev_1 in zip(ev_2h, ev_2h[1:]):
    diff_time.append(ev_1["eventSec"] - ev["eventSec"])

t_btw_eventi = round(sum(diff_time)/len(diff_time), 4)

with open("esercizio14.csv", "w") as f:
    f.write(";".join(["t_btw_eventi"]))
    f.write("\n")
    f.write(str(t_btw_eventi))
    f.write("\n")
