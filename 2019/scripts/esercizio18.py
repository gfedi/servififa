import json as js

with open("events.json") as events:
    events_dict = js.load(events)

n_pass_accurati = len(
    [x for x in events_dict
        if 'pass' in x['subEventName'] and 1801 in [y['id']
                                                    for y
                                                    in x['tags']] and
            x['playerId'] == 3323 and x['matchId'] == 2576302 and
                x['positions'][0]['x'] >= 50 and
                    x['positions'][0]['x'] <= 100 and (
                        (x['eventSec'] > 1800 and x['matchPeriod'] == '1H') or
                            x['matchPeriod'] == '2H')])

with open("esercizio18.csv", "w") as f:
    f.write("n_pass_accurati\n")
    f.write("%s\n" % str(n_pass_accurati))
