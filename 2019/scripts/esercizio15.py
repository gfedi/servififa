import json as js

csv_headers = ['tempo', 'momento', 'distanza']

with open("events.json") as events:
    events_dict = js.load(events)

shots = [
    {csv_headers[0]: x['matchPeriod'],
     csv_headers[1]: round(x['eventSec'], 2),
     csv_headers[2]: x['positions'][1]['x'] - x['positions'][0]['x']}
    for x in events_dict
    if x['subEventName'] == 'Shot' and 
        x['matchId'] == 2576302 and
            x['positions'][1]['x'] == 100]

shots = sorted(
    [s for s in shots if s['tempo'] == '2H'],
    key=lambda k: k['momento'],
    reverse=True) + \
        sorted(
            [s for s in shots if s['tempo'] == '1H'],
            key=lambda k: k['momento'],
            reverse=True)

with open("esercizio15.csv", "w") as f:
    f.write(";".join(csv_headers) + "\n")
    for shot in shots:
        f.write(";".join([str(v) for k, v in shot.items()]) + "\n")
