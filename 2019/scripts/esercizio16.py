import json as js

csv_headers = ['playerId', 'nationality', 'n_pass_sbagliati']

with open("events.json") as events:
    events_dict = js.load(events)

with open("players.json", encoding='utf-8') as players:
    players_dict = js.load(players)

list_players_in_match = {
    x['playerId'] for x in events_dict
    if x['matchId'] == 2576302 and x['playerId'] != 0}

wrong_passes = []
for player in [x for x in players_dict if x['wyId'] in list_players_in_match]:
    n_wrong_passes = len([
        x for x in events_dict
        if 'pass' in x['subEventName'] and
        1802 in [y['id'] for y in x['tags']] and
        x['matchId'] == 2576302 and
        x['playerId'] == player['wyId']])
    wrong_passes.append(
        (str(player['wyId']),
         player['birthArea']['name'],
         str(n_wrong_passes)))


wrong_passes_best = sorted(
    wrong_passes, key=lambda x: int(x[2]), reverse=True)[0:3]

wrong_passes_best.sort(key=lambda x: int(x[0]))

with open("esercizio16.csv", "w") as f:
    f.write(";".join(csv_headers) + "\n")
    for wrong_pass in wrong_passes_best:
        f.write(";".join(wrong_pass) + "\n")
