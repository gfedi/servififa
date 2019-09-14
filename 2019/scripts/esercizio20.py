import json as js

csv_headers = ['playerId', 'n_parate']

with open("events.json") as events:
    events_dict = js.load(events)

save_attempt = [x['playerId'] for x in events_dict 
                if x['subEventName'] == 'Save attempt' and
                    x['matchId'] == 2576302]
n_save_attempt = [
    (k, v) for k, v in {x:save_attempt.count(x) for x in save_attempt}.items()]

n_save_attempt.sort(key=lambda x: x[0])

n_save_attempt.sort(key=lambda x: x[1])

with open("esercizio20.csv", "w") as f:
    f.write(";".join(csv_headers) + "\n")
    for x in n_save_attempt:
        f.write("%s;%s\n" % (x[0], x[1]))
