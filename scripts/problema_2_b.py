#!/usr/bin/python3

import requests
from collections import defaultdict
import pandas as pd
import numpy as np

PLAYERS_URL = ("https://raw.githubusercontent.com/mesosbrodleto/"
              "soccerDataChallenge/master/players.json")

EVENTS_URL = ("https://raw.githubusercontent.com/mesosbrodleto/"
              "soccerDataChallenge/master/worldCup-final.json")


def get_players():
    """
    get the list of players
    """

    return requests.get(PLAYERS_URL).json()


def get_events():
    """
    get the list of events in the match
    """

    return requests.get(EVENTS_URL).json()


def main():
    events = get_events()
    players = get_players()

    # print(players)

    duels = defaultdict(list)
    for e in events:
        if e['subEventName'] == 'Ground defending duel':
            # se giocatore ha vinto un tackle flag=1 altrimenti flag=0
            if {'id': 703} in e['tags']:
                duels[e['playerId']].append(1)
            else:
                duels[e['playerId']].append(0)    
    # seleziona giocatori con tackle > 2 
    duels_sel = {k:v for k,v in duels.items() if len(v)>2 }
    # associa giocatori con tackle vinti (somma delle flag tackle vinti)
    duels_sel_won = {k:sum(v) for k,v in duels_sel.items()}
    # calcola valore quarto quartile 
    vals = np.array([v for k,v in duels_sel_won.items()])
    perc_75 = np.percentile(vals, 75)
    # seleziona giocatori con tackle > quarto quartile
    duels_final = {k:v for k,v in duels_sel_won.items() if v>perc_75}
    # associa id giocatore e nome
    player_name_id = dict()
    for p in players:
        player_name_id[p['playerId']] = p['name']
    # salva soluzione in un dict
    solution = []
    for k,v in duels_final.items():
        solution.append({'identificativo_calciatore': k, 'nome_calciatore': player_name_id[k], 'tackle_vinti': v})
    # salva su csv
    solution_df = pd.DataFrame(solution)
    solution_df.to_csv('problema_2_b.csv', index=False)

if __name__ == "__main__":
    main()