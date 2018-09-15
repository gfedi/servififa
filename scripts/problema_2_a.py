#!/usr/bin/python3

import requests
import pandas as pd
from numpy import array


PLAYERS_URL = ("https://raw.githubusercontent.com/mesosbrodleto/"
              "soccerDataChallenge/master/players.json")
EVENTS_URL = ("https://raw.githubusercontent.com/mesosbrodleto/"
              "soccerDataChallenge/master/worldCup-final.json")
ACCURATE_TAG = 1801


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
    match = get_events()
    players = get_players()

    events = pd.DataFrame(match,
                          columns=['teamId', 'playerId', 'tags', 'eventId'])

    passes_x_team = events.loc[events['eventId'] == 8].groupby(
        ['teamId', 'playerId']).count()['tags'].to_dict()

    accurate_passes_x_team = events.loc[(events['eventId'] == 8) & \
        (events['tags'].apply(lambda x: {"id": ACCURATE_TAG} in x))].groupby(
            ['teamId', 'playerId']).count()['tags'].to_dict()

    results_d = list()
    for t in events['teamId'].unique():
        accuracy = array([accurate_passes_x_team[k] / float(passes_x_team[k])
                          for k in accurate_passes_x_team if t in k])
        results_d.append(
            {'nome_squadra': t,
             'accuratezza_media_dei_passaggi' : accuracy.mean(),
             'standard_deviation_accuratezza_media_dei_passaggi' : accuracy.std()})
    pd.DataFrame(results_d).to_csv('problema_2_a.csv', index=False)


if __name__ == "__main__":
    main()
