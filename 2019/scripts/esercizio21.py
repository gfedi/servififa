import json as js

csv_headers = ['tipo_tiro', 'playerId', 'n_tiri']

with open("events.json") as events:
    events_dict = js.load(events)

list_players_in_match = {
    x['playerId'] for x in events_dict
    if x['matchId'] == 2576302 and x['playerId'] != 0}

shots = [
    ('1209' if 1209 in [y['id'] for y in x['tags']] else \
        ('1210' if 1210 in [y['id'] for y in x['tags']] else '1218'),
     x['playerId'])
    for x in events_dict
    if x['subEventName'] == 'Shot' and 
        x['matchId'] == 2576302 and
            x['positions'][1]['x'] == 100 and
                (1209 in [y['id'] for y in x['tags']] or
                    1210 in [y['id'] for y in x['tags']] or
                        1218 in [y['id'] for y in x['tags']])]

shots = [(s[0], s[1], shots.count(s)) for s in shots]

shots = sorted(shots, key=lambda k: k[0])

shots = sorted(shots, key=lambda k: k[1])

shots = sorted(shots, key=lambda k: k[2])

with open("esercizio21.csv", "w") as f:
    f.write(";".join(csv_headers) + "\n")
    for shot in shots:
        f.write(";".join([str(v) for v in shot]) + "\n")
