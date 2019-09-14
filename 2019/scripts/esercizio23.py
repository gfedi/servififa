import json as js

with open("events.json") as events:
    events_dict = js.load(events)



tempi = [[e["eventSec"],e['matchPeriod']] for e in events_dict]
sec1h = [e[0] for e in tempi if e[1]=="1H"]
sec2h = [e[0] for e in tempi if e[1]=="2H"]


reg = []
for period in ["1H","2H"]:
  for temp in range(int(max(sec1h)/600)+1):
     eventi = len([e for e in events_dict if e["matchPeriod"]==period and e["eventSec"]>temp*600 and e["eventSec"]<(temp+1)*600])
     tempo=""
     if period=="1H": tempo="primo"
     if period=="2H": tempo="secondo"
     reg.append((temp, tempo, eventi))



with open("esercizio23.csv", "w") as f:
    f.write(";".join(["slot","tempo","n_events"]))
    f.write("\n")
    for el in reg:
        f.write(";".join([str(e) for e in el]))
        f.write("\n")

